from selenium import webdriver
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# Открываем первую вкладку
driver.get("https://example.com")
time.sleep(2)  # Для наглядности делаем паузу

# Открываем новую вкладку с помощью execute_script
driver.execute_script("window.open('https://google.com', '_blank');")
time.sleep(2)  # Для наглядности делаем паузу

# Получаем все открытые вкладки
tabs = driver.window_handles

# Переключаемся на вторую вкладку (по индексу 1)
driver.switch_to.window(tabs[1])
time.sleep(2)  # Для наглядности делаем паузу

# Закрываем текущую (вторую) вкладку
driver.close()

# Переключаемся обратно на первую вкладку (по индексу 0)
driver.switch_to.window(tabs[0])

# Закрытие браузера
driver.quit()