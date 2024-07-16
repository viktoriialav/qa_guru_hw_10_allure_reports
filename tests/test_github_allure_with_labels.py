import allure
from allure_commons.types import Severity, LabelType
from selene import browser, have, be, by


@allure.title('Test issue tab')
@allure.description('This test allows to check the existence of special number of the issue')
@allure.tag('Issues', 'Test')
@allure.severity(severity_level=Severity.TRIVIAL)
@allure.label(LabelType.LANGUAGE, 'python')
@allure.label(LabelType.FRAMEWORK, 'pytest')
@allure.label('owner', 'viktoriialav')
@allure.feature('Issues')
@allure.story('An authorized user can create a new issue in the repository')
@allure.link('https://github.com', 'Testing')
def test_github_issue_tab_context_steps():
    with allure.step('Open the page'):
        browser.open('/')

    with allure.step('Search for the repository'):
        browser.element('[data-target="qbsearch-input.inputButton"]').click()
        browser.element('#query-builder-test').send_keys('viktoriialav/qa_guru_lesson_10').press_enter()

    with allure.step('Go to the link of repository'):
        browser.element(by.link_text('viktoriialav/qa_guru_lesson_10')).click()

    with allure.step('Open the tab Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Check for the issue #2'):
        browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)