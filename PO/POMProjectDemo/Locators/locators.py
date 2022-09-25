class Locators():

    # Login page objects

    username_texbox_name = "username"
    password_texbox_name = "password"
    login_button_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    invalidUsername_message_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]"


    # Home page objects

    welcome_link_xpath = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    logout_link_text = "Logout"