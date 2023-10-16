import asyncio
import logging
import traceback
import pyppeteer.errors
import time

logger = logging.getLogger(__name__)

async def handle_cookie_accept_xpath(
        page=None, accept_cookie_xpath=None,
        accept_cookie_button=True, max_retries=0
) -> tuple[bool, str or None]:
    """
    Generate the XPath for the cookie accept button on the given URL.
    Additionally, click on the accept cookie button if "accept_cookie_button"
    is True(default).

    Args:
        page: The Pyppeteer page instance.
        accept_cookie_xpath: XPath stored in the database or explicitly provided.
        accept_cookie_button: Set to True to click on the accept cookie button.
        max_retries: The maximum number of times to retry if an exception is raised.

    Returns:
        Tuple:
            bool: True if the button is accepted/clicked, False otherwise.
            str/None: XPath if found, None if not.

    Usage:
    click_success, xpath_generated = await handle_cookie_accept_xpath(
                                    accept_cookie_xpath=accept_cookie_xpath,
                                    page=page, accept_cookie_button=True)

    TODO: 
        * Add parameter to decline cookie consent button.
        * Dynamic search_texts: Allow users to customize the list of search texts for cookie acceptance.
                                as per need/scenario.
    """

    async def accept_xpath_button(cookie_xpath=None) -> tuple[bool, str or None]:
        """
        Helper function to click on the cookie consent button.
        Args:
            cookie_xpath: The XPath of the cookie consent button.

        Returns:
            Tuple: Same as the parent function.
        """
        try:
            if cookie_xpath and isinstance(cookie_xpath, str):
                accept_cookie_xpath_button = await page.xpath(cookie_xpath)
                click_success = False
                if accept_cookie_xpath_button:
                    done, pending = await asyncio.wait([
                        accept_cookie_xpath_button[0].click(),
                        page.waitForNavigation(
                            {"waitUntil": ["load", "domcontentloaded"]},
                            timeout=100000),
                    ])
                    logger.info(
                        f"For consent button: {cookie_xpath}, Done: {done}, "
                        f"Pending: {pending}."
                    )
                    if done:
                        click_success = True
                    return click_success, cookie_xpath

        except Exception as err:
            logger.error(
                f"Unexpected Error: {err} with Traceback: {traceback.format_exc()}, "
                 "while generating xpath for cookie button"
            )
            return False, xpath

        return False, xpath

    xpath = None
    success = False

    if page:
        if accept_cookie_xpath and accept_cookie_button:
            success, xpath = await accept_xpath_button(cookie_xpath=accept_cookie_xpath)
        
        else:
            for attempt in range(0, max_retries + 1):
                try:
                    # Sometimes pyppeteer doesn't load the content.
                    # This fixes the issue to large extend.
                    await page.xpath("//body/descendant-or-self::*")
                    time.sleep(2)

                    # Find the "anchor or button" element with text
                    # "Accept All Cookies", "Accept Cookies", "Accept All" etc...
                    # In case you find a new text type button, just add it to the
                    # searchTexts list.
                    xpath = await page.evaluate("""() => {
                        const searchTexts = ["Accept All Cookies", "Accept Cookies", "Accept All", "Accept and continue"];
                        const results = [];
                        const aElements = document.querySelectorAll('a');
                        const buttonElements = document.querySelectorAll('button');
                    
                        function isValidElement(element) {
                            const text = element.textContent.trim();
                            return searchTexts.includes(text);
                        }
                    
                        aElements.forEach(element => {
                            const hasOnlyText = element.children.length === 0 || (element.children.length === 1 && element.children[0].nodeType === Node.TEXT_NODE);
                            if (isValidElement(element) && hasOnlyText) {
                                results.push(element);
                            }
                        });
                    
                        buttonElements.forEach(element => {
                            const hasOnlyText = element.children.length === 0 || (element.children.length === 1 && element.children[0].nodeType === Node.TEXT_NODE);
                            if (isValidElement(element) && hasOnlyText) {
                                results.push(element);
                            }
                        });
                    
                        return results.map(result => {
                            const selfXpath = document.evaluate(
                                `ancestor-or-self::*[self::a or self::button][1]`,
                                result,
                                null,
                                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                null
                            );
                            const parentXpath = document.evaluate(
                                `ancestor-or-self::*[self::a or self::button][1]/parent::*[1]`,
                                result,
                                null,
                                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                null
                            );
                            const paths = [];
                            for (let i = 0; i < selfXpath.snapshotLength; i++) {
                                const selfNode = selfXpath.snapshotItem(i);
                                const parentNode = parentXpath.snapshotItem(i);
                                const tagName = selfNode.tagName.toLowerCase();
                                const id = selfNode.id ? `[@id="${selfNode.id}"]` : '';
                                const className = selfNode.className ? `[@class="${selfNode.className}"]` : '';
                                const selfPath = `//${tagName}${id}${className}`;
                                if (selfNode !== parentNode) {
                                    const parentTagName = parentNode.tagName.toLowerCase();
                                    const parentId = parentNode.id ? `[@id="${parentNode.id}"]` : '';
                                    const parentClassName = parentNode.className ? `[@class="${parentNode.className}"]` : '';
                                    const parentPath = `//${parentTagName}${parentId}${parentClassName}`;
                                    paths.push(`${parentPath}${selfPath}`);
                                } else {
                                    paths.push(selfPath);
                                }
                            }
                            return paths.join(' | ');
                        }).join(' | ');
                    }""")

                    if accept_cookie_button:
                        try:
                            success, _ = await accept_xpath_button(cookie_xpath=xpath)
                        except Exception as e:
                            logger.error("generate_cookie_accept_xpath! Ran into Error: "
                                         f"{e} with Traceback: {traceback.format_exc()}, "
                                         "while generating xpath for cookie button")
                            pass

                except Exception as err:
                    logger.info(f"While evaluating cookie xpath, Error: {err}")
                    if attempt < max_retries:
                        time.sleep(3)
    else:
        logger.error("Page instance not provided.")

    return success, xpath
