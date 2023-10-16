import asyncio
import unittest
from unittest import IsolatedAsyncioTestCase
from cookie_acceptance_handler import handle_cookie_accept_xpath
from pyppeteer import launch

class TestCookieAcceptance(IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.browser = await launch(headless=True, args=[
            '--window-size=1920,1080',
            "--no-sandbox",
            "--incognito"
        ])
        self.page = await self.browser.newPage()
        await self.page.goto('http://www.example.com')

    async def asyncTearDown(self):
        await self.page.close()
        await self.browser.close()

    async def test_accept_cookie_xpath(self):
        result, xpath = await handle_cookie_accept_xpath(page=self.page, accept_cookie_xpath="your_xpath_here")
        self.assertTrue(result)  # Modify this based on your expected result
        self.assertIsNotNone(xpath)  # Modify this based on your expected result

if __name__ == "__main__":
    unittest.main()

