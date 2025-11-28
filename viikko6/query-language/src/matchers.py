class QueryBuilder:
    def __init__(self, matcher=None):
        self._matcher = matcher if matcher else All()

    def build(self):
        return self._matcher

    def plays_in(self, team):
        new_matcher = PlaysIn(team)
        combined_matcher = And(self._matcher, new_matcher)
        return QueryBuilder(combined_matcher)

    def has_at_least(self, value, attr):
        new_matcher = HasAtLeast(value, attr)
        combined_matcher = And(self._matcher, new_matcher)
        return QueryBuilder(combined_matcher)

    def has_fewer_than(self, value, attr):
        new_matcher = HasFewerThan(value, attr)
        combined_matcher = And(self._matcher, new_matcher)
        return QueryBuilder(combined_matcher)
    
    def one_of(self, *queries):
        matchers = [q.build() for q in queries]
        or_matcher = Or(*matchers)
        combined_matcher = And(self._matcher, or_matcher)
        return QueryBuilder(combined_matcher)


class All:
    def test(self, player):
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False