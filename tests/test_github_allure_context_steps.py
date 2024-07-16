import allure
from selene import browser, have, be, by


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

