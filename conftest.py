import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from Pages.SbisPages.SbisMainPage import SbisMainHelper
from Pages.SbisPages.SbisContactsPage import SbisContactsHelper
from Pages.SbisPages.SbisDownloadPage import SbisDownloadHelper
from Pages.TensorPages.TensorMainPage import TensorMainHelper
from Pages.TensorPages.TensorAboutPage import TensorAboutHelper
from TestsConf import computer_region, test_region
from OtherFunctions import Functions


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome(options)
    yield driver
    driver.quit()


def test_script_1(browser):
    sbis_main_page = SbisMainHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_contacts()
    sbis_contacts_page = SbisContactsHelper(browser)
    sbis_contacts_page.click_for_clients()
    sbis_contacts_page.click_for_clients_tensor()

    tensor_main_page = TensorMainHelper(browser)
    # Смена вкладки на нужную с проверкой по ссылке
    tensor_main_page.switch_handle()
    tensor_main_page.click_man_power_about()

    tensor_about_page = TensorAboutHelper(browser)
    # Сверка url страницы
    assert tensor_about_page.check_url()
    # Парсинг размеров изображений
    sizes = [
        {"width": image.get_attribute("width"), "height": image.get_attribute("height")}
        for image in tensor_about_page.get_work_images_blocks()
    ]

    # Сравнение всех размеров с первым элементом
    assert all(sizes[0] == size for size in sizes)


def test_script_2(browser):
    sbis_main_page = SbisMainHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_contacts()
    sbis_contacts_page = SbisContactsHelper(browser)

    # Проверка автоопределения региона
    assert sbis_contacts_page.get_region_element().text == computer_region.get("name")
    # Проверка наличия партнеров
    assert sbis_contacts_page.get_parters()
    # Выбор региона
    sbis_contacts_page.select_region(test_region.get("name"))
    sbis_contacts_page.wait_url_pattern(test_region.get("url"))
    assert test_region.get("name") in sbis_contacts_page.get_title()
    assert sbis_contacts_page.get_parters()


def test_script_3(browser):
    sbis_main_page = SbisMainHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.click_download()

    # Переход на страницу загрузок
    sbis_download_page = SbisDownloadHelper(browser)
    # Нажимаем на плагин
    sbis_download_page.click_plugin()
    # Нажимаем на Windows чтобы точно оказаться в нужном месте
    sbis_download_page.click_windows_link()
    # Получаем ссылку для загрузки
    link = sbis_download_page.get_plugin_download_link()
    # При помощи регулярного выражения парсим размер с сайта
    size = sbis_download_page.get_plugin_size()
    # Скачиваем файл и сохраняем в директории проекта
    # Получаем размер файла, конвертируем в МБ и задаем точность в 2 числа после запятой
    file_size = round(Functions.download_file(link).__sizeof__() / 1048576, 2)
    # Сравниваем размер с сайта и размер скачанного файла
    assert file_size == size
