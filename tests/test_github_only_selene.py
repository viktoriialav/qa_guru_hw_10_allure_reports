from selene import browser, by, have, be


def test_github_issues_tab():
    browser.open('/')

    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element('#query-builder-test').send_keys('viktoriialav/qa_guru_lesson_10').press_enter()

    browser.element(by.link_text('viktoriialav/qa_guru_lesson_10')).click()

    browser.element('#issues-tab').click()

    browser.all('.opened-by').element_by(have.text('#2')).should(be.visible)
