import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        login_button = self.driver.find_element_by_css_selector(".btn")

        # Replace with your test email
        email_input.send_keys("example@example.com")
        # Replace with your test password
        password_input.send_keys("password123")
        login_button.click()

        # Add assertions to verify the login functionality
        # For example:
        welcome_message = self.driver.find_element_by_css_selector(
            ".faculty-heading").text
        self.assertEqual(welcome_message, "Welcome, John Doe")

    def test_pressedpass(driver):
        # Replace with the URL of your application
        driver.get('http://localhost:5173')

        # Find the email input field and enter the email
        email_input = driver.find_element_by_css_selector(
            'input[name="passemail"]')
        email_input.send_keys('test@example.com')

        # Find the submit button and click it
        submit_button = driver.find_element_by_css_selector('button')
        submit_button.click()

        # Wait for the API request to complete and the response to be displayed
        time.sleep(2)

        # Verify the resulting behavior based on the API response
        response_element = driver.find_element_by_css_selector('.response')
        assert response_element.text == 'Forgot Password Successful'

        # Other assertions and verifications as needed

        # Example: Verify the URL after the action is completed
        assert driver.current_url == 'http://localhost:5173/reset-password'

        # Example: Verify an element on the next page
        welcome_message = driver.find_element_by_css_selector(
            '.welcome-message')
        assert welcome_message.text == 'Welcome, test@example.com'

    def test_forgot_password(self):
        self.driver.get('http://localhost:8000/forgot-password')

        email_input = self.driver.find_element_by_css_selector(
            'input[name="passemail"]')
        email_input.send_keys('test@example.com')

        password1_input = self.driver.find_element_by_css_selector(
            'input[name="pass1"]')
        password1_input.send_keys('password123')

        password2_input = self.driver.find_element_by_css_selector(
            'input[name="pass2"]')
        password2_input.send_keys('password123')

        submit_button = self.driver.find_element_by_css_selector('button')
        submit_button.click()

        time.sleep(2)

        response_element = self.driver.find_element_by_css_selector(
            '.response')
        self.assertEqual(response_element.text, 'Password reset successful')

    def test_dashboard(self):
        # Wait for the dashboard content to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dashboard-content")))

        # Get the dashboard title
        title_element = self.driver.find_element(
            By.CLASS_NAME, "dashboard-title")
        title = title_element.text
        self.assertEqual(title, "Welcome, John Doe!")

        # Get the dashboard stats
        stat_elements = self.driver.find_elements(
            By.CLASS_NAME, "dashboard-stat-value")
        total_quizzes = stat_elements[0].text
        quizzes_completed = stat_elements[1].text
        correct_answers = stat_elements[2].text
        self.assertEqual(total_quizzes, "10")
        self.assertEqual(quizzes_completed, "5")
        self.assertEqual(correct_answers, "25")

        # Get the quiz items
        quiz_items = self.driver.find_elements(By.CLASS_NAME, "quiz-item")
        self.assertEqual(len(quiz_items), 3)  # Assuming there are 3 quizzes

        # Iterate over quiz items and check their content
        for quiz_item in quiz_items:
            quiz_title_element = quiz_item.find_element(
                By.CLASS_NAME, "quiz-link")
            quiz_title = quiz_title_element.text
            self.assertTrue(quiz_title)  # Check if the quiz title is not empty

            quiz_meta_lines = quiz_item.find_elements(
                By.CLASS_NAME, "quiz-meta-line")
            # Assuming there are 2 meta lines
            self.assertEqual(len(quiz_meta_lines), 2)

            # Get the values from meta lines
            questions_label = quiz_meta_lines[0].find_element(
                By.CLASS_NAME, "quiz-meta-label").text
            questions_value = quiz_meta_lines[0].find_element(
                By.CLASS_NAME, "quiz-meta-value").text
            duration_label = quiz_meta_lines[1].find_element(
                By.CLASS_NAME, "quiz-meta-label").text
            duration_value = quiz_meta_lines[1].find_element(
                By.CLASS_NAME, "quiz-meta-value").text

            self.assertEqual(questions_label, "Questions:")
            self.assertTrue(questions_value)
            self.assertEqual(duration_label, "Duration:")
            self.assertTrue(duration_value.endswith("mins"))

        # Check the presence of the progress bar
        progress_bar = self.driver.find_element(By.CLASS_NAME, "progress-bar")
        self.assertTrue(progress_bar.is_displayed())

        progress_bar = self.driver.find_element(By.CLASS_NAME, "progress-bar")
        self.assertTrue(progress_bar.is_displayed())

    def test_start_quiz(self):
        # Click the "Start Quiz" button
        start_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        start_button.click()

        # Wait for the quiz page to load
        WebDriverWait(self.driver, 10).until(EC.title_contains("Quiz"))

        # Assert that the user is redirected to the quiz page
        self.assertIn("quiz", self.driver.current_url)

    def test_create_quiz(self):
        # Fill in the form values
        question_desc_input = self.driver.find_element(By.ID, "question")
        question_desc_input.send_keys("What is the capital of France?")

        option_a_input = self.driver.find_element(By.ID, "optionA")
        option_a_input.send_keys("Paris")

        option_b_input = self.driver.find_element(By.ID, "optionB")
        option_b_input.send_keys("London")

        option_c_input = self.driver.find_element(By.ID, "optionC")
        option_c_input.send_keys("Berlin")

        # Click the "Save and close" button
        submit_button = self.driver.find_element(
            By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Wait for the quiz to be saved (you can add additional assertions or checks here)
        # For example, you can wait for a success message or check the database for the created quiz

        # Assert that the question description is saved correctly
        question_saved = self.driver.find_element(
            By.CLASS_NAME, "saved-question-description").text
        self.assertEqual(question_saved, "What is the capital of France?")

    def test_quiz_page(self):
        # Assuming you have already logged in and reached the quiz page

        # Wait for the timer to start
        timer_element = self.driver.find_element(
            By.CLASS_NAME, "home-container")
        self.assertTrue(timer_element.is_displayed())

        # Verify the quiz name
        quiz_name_element = self.driver.find_element(
            By.CLASS_NAME, "home-text27")
        self.assertEqual(quiz_name_element.text, "Your Quiz Name")

        # Answer the first question
        option_a_element = self.driver.find_element(
            By.XPATH, "//input[@value='optionA']")
        option_a_element.click()

        # Click "CONTINUE"
        continue_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'CONTINUE')]")
        continue_button.click()

        # Answer the second question
        option_b_element = self.driver.find_element(
            By.XPATH, "//input[@value='optionB']")
        option_b_element.click()

        # Click "SUBMIT"
        submit_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'SUBMIT')]")
        submit_button.click()

        # Wait for the score confirmation message
        score_message = self.driver.switch_to.alert.text
        self.assertIn("Your score is", score_message)

        # Confirm the score
        self.driver.switch_to.alert.accept()

        # Verify the navigation to the dashboard
        self.assertEqual(self.driver.current_url,
                         "http://localhost:8000/dashboard?mail=indu@gmail.com")


if __name__ == "__main__":
    unittest.main()
