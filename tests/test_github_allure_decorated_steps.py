import allure
from selene import browser, have, be, by


def test_github_issue_tab_decorated_steps():
    open_main_page()
    search_for_repository('viktoriialav/qa_guru_lesson_10')
    go_to_repository('viktoriialav/qa_guru_lesson_10')
    open_issue_tab()
    check_issue_number('2')


@allure.step('Open the page')
def open_main_page():
    browser.open('/')


@allure.step('Search for the repository {repo}')
def search_for_repository(repo):
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Go to the link of repository {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open the tab Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Check for the issue #{number}')
def check_issue_number(number):
    browser.all('.opened-by').element_by(have.text(f'#{number}')).should(be.visible)

