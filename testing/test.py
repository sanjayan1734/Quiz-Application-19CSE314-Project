import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


class TestQuizApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Replace with your actual URL
        self.driver.get("http://localhost:5173/login")
        email_input = self.driver.find_element(by=By.NAME, value='logemail')
        password_input = self.driver.find_element(by=By.NAME, value='logpass')
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[class='btn mt-4']")

        # Replace with your test email
        email_input.send_keys("harish251102@gmail.com")
        # Replace with your test password
        password_input.send_keys("harish02")
        login_button.click()

    def test_homepage_content(self):
        self.driver.get("http://localhost:5173")  # Replace with your app's URL

        # Verify the content of the homepage
        title = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(title.text, "Your favorite place for Quizzes")

        description = self.driver.find_element(
            By.CSS_SELECTOR, "p.text-white-75")
        self.assertEqual(
            description.text, "Welcome to our quiz app! Perfect way to satisfy your thirst for knowledge and have fun at the same time.")

        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "div.Login-Button button")
        self.assertTrue(login_button.is_displayed())

    def test_about_section(self):
        self.driver.get("http://localhost:5173")  # Replace with your app's URL

        # Verify the content of the about section
        about_heading = self.driver.find_element(
            By.CSS_SELECTOR, "section#about h2")
        self.assertEqual(about_heading.text, "We've got what you need!")

        about_description = self.driver.find_element(
            By.CSS_SELECTOR, "section#about p.text-white-75")
        self.assertEqual(about_description.text,
                         "Our app is easy to use and navigate, with a simple and intuitive interface. We offer a huge selection of quizzes on a wide range of topics")

    # # Perform any additional assertions or actions as needed

    # # def test_forgot_password(self):
    # #     self.driver.get('http://localhost:5173/forgotpwd')

    # #     email_input = self.driver.find_element_by_css_selector(
    # #         'input[name="passemail"]')
    # #     email_input.send_keys('test@example.com')

    # #     password1_input = self.driver.find_element_by_css_selector(
    # #         'input[name="pass1"]')
    # #     password1_input.send_keys('password123')

    # #     password2_input = self.driver.find_element_by_css_selector(
    # #         'input[name="pass2"]')
    # #     password2_input.send_keys('password123')

    # #     submit_button = self.driver.find_element_by_css_selector('button')
    # #     submit_button.click()

    # #     time.sleep(2)

    # #     response_element = self.driver.find_element_by_css_selector(
    # #         '.response')
    # #     self.assertEqual(response_element.text, 'Password reset successful')

    def test_pressedpass(self):
        # Replace with the URL of your application
        self.driver.get('http://localhost:5173/forgotpwd')

        # Find the email input field and enter the email
        email_input = self.driver.find_element(by=By.NAME, value='passemail')
        email_input.send_keys('test@example.com')

        # Find the submit button and click it
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[class='btn mt-4']")
        submit_button.click()

        # Wait for the API request to complete and the response to be displayed
        time.sleep(2)

    def test_dashboard_content(self):
        # Log in
        # Replace with actual credentials
        self.test_login()

        # Wait for the dashboard content to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dashboard-content")))

    #     # Get the dashboard title

    #     # Get the dashboard stats

    # # Check if the quiz grid is present
    #     quiz_grid = self.driver.find_element(By.CLASS_NAME, "quiz-grid")
    #     self.assertTrue(quiz_grid.is_displayed())

    #     # Check if the progress bar is present
    #     progress_bar = self.driver.find_element(By.CLASS_NAME, "progress-bar")
    #     self.assertTrue(progress_bar.is_displayed())

    #     # Check if the notification list is present
    #     notification_list = self.driver.find_element(
    #         By.CLASS_NAME, "notification-list")
    #     self.assertTrue(notification_list.is_displayed())

    #     # Check if the recent discussion section is present
    #     recent_discussion = self.driver.find_element(
    #         By.CLASS_NAME, "recent-discussion")
    #     self.assertTrue(recent_discussion.is_displayed())

    #     # Check if the upcoming events section is present
    #     event_grid = self.driver.find_element(By.CLASS_NAME, "event-grid")
    #     self.assertTrue(event_grid.is_displayed())

    #     # Check if the register button for the first event is present
    #     register_button = self.driver.find_element(
    #         By.CSS_SELECTOR, ".event-item:first-child .event-register-button")
    #     self.assertTrue(register_button.is_displayed())

    #     # Check if the details button for the first event is present
    #     details_button = self.driver.find_element(
    #         By.CSS_SELECTOR, ".event-item:first-child .event-details-button")
    #     self.assertTrue(details_button.is_displayed())

    # def test_create_quiz(self):
    #     # Fill in the form values
    #     question_desc_input = self.driver.find_element(By.ID, "question")
    #     question_desc_input.send_keys("What is the capital of France?")

    #     option_a_input = self.driver.find_element(By.ID, "optionA")
    #     option_a_input.send_keys("Paris")

    #     option_b_input = self.driver.find_element(By.ID, "optionB")
    #     option_b_input.send_keys("London")

    #     option_c_input = self.driver.find_element(By.ID, "optionC")
    #     option_c_input.send_keys("Berlin")

    #     # Click the "Save and close" button
    #     submit_button = self.driver.find_element(
    #         By.XPATH, "//button[@type='submit']")
    #     submit_button.click()

    #     # Wait for the quiz to be saved (you can add additional assertions or checks here)
    #     # For example, you can wait for a success message or check the database for the created quiz

    #     # Assert that the question description is saved correctly
    #     question_saved = self.driver.find_element(
    #         By.CLASS_NAME, "saved-question-description").text
    #     self.assertEqual(question_saved, "What is the capital of France?")
    def test_quiz_page(self):
        # Log in

        self.test_login()  # Replace with actual credentials
        dashboard_url = self.driver.current_url
        # Assuming you have already logged in and reached the quiz page

        # Get the quiz items
        quiz_item = self.driver.find_element(By.CLASS_NAME, "quiz-item")

        # Iterate over quiz items and click on each quiz

        # Store the URL of the dashboard page

        # Click on the quiz link
        quiz_link = quiz_item.find_element(By.CLASS_NAME, "quiz-link")
        quiz_link.click()

        # Wait for the timer to start
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "home-container")))

        # Answer the questions
        question_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, ".question button")
        question_count = len(question_buttons)
        for i in range(question_count):
            button = question_buttons[i]
            button.click()
            # Wait for the next question to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".question button")))

            # Click "Continue" button
            continue_button = self.driver.find_element(
                By.CLASS_NAME, "home-group7")
            continue_button.click()
        continue_button.click()
        continue_button.click()
        # Wait for the "Submit" button to appear

        # Click "Submit" button
        submit_button = self.driver.find_element(
            By.CLASS_NAME, "home-group7")
        submit_button.click()

        # Wait for the score confirmation message
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        score_message = self.driver.switch_to.alert.text
        self.assertIn("Your score is", score_message)

        # Confirm the score
        self.driver.switch_to.alert.accept()


if __name__ == "_main_":
    unittest.main()
