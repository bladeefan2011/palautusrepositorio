*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Text    username    eetos
    Input Password    password    salasana123
    Input Password    password_confirmation    salasana123
    Click Button    Register
    
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Input Text    username    ee
    Input Password    password    salasana123
    Input Password    password_confirmation    salasana123
    Click Button    Register
    
    Register Page Should Be Open
    Page Should Contain    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Text    username    eetos
    Input Password    password    sala123
    Input Password    password_confirmation    sala123
    Click Button    Register
    
    Register Page Should Be Open
    Page Should Contain    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Input Text    username    eetos
    Input Password    password    salasanat
    Input Password    password_confirmation    salasanat
    Click Button    Register
    
    Register Page Should Be Open
    Page Should Contain    Password must not be all letters

Register With Nonmatching Password And Password Confirmation
    Input Text    username    eetos
    Input Password    password    salasana123
    Input Password    password_confirmation    salasana1234
    Click Button    Register
    
    Register Page Should Be Open
    Page Should Contain    Passwords do not match

Register With Username That Is Already In Use
    Create User    testaaja    salasana123
    
    Input Text    username    testaaja
    Input Password    password    eri_salasana123
    Input Password    password_confirmation    eri_salasana123
    Click Button    Register
    
    Register Page Should Be Open
    Page Should Contain    Username is already in use

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
