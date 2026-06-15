from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Откройте страницу
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1
    cookie_user1 = {
        "name": "SESSION",
        "value": "ZThjMWJhZTQtNmFlOC00ODE2LTkxNTYtN2VlYjA0YzhmODky"
    }

    driver.add_cookie(cookie_user1)
    driver.refresh()

    # Проверяем, что cookie установлена
    assert driver.get_cookie("SESSION") is not None

    # Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/12kiborg")
    user1_url = driver.current_url

    # Разлогиньтесь (очистите cookie)
    driver.delete_all_cookies()

    # Откройте главную страницу снова
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 2
    cookie_user2 = {
        "name": "SESSION",
        "value": "ZDdiZWY0MzItNTM4ZC00ZmQwLWI5YjAtY2I0NjM0ZmY1YzEy"
    }

    driver.add_cookie(cookie_user2)
    driver.refresh()

    # Проверяем, что cookie установлена
    assert driver.get_cookie("SESSION") is not None

    # Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/kiborg12")
    user2_url = driver.current_url

    # Проверьте, что URL различаются
    assert user1_url != user2_url

    driver.quit()
