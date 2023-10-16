"""This is a mobile device test for Chromium-based browsers (such as MS Edge)
Usage:  pytest test_skype_site.py --mobile --edge

Default mobile settings for User Agent and Device Metrics if not specified:
        User Agent:   --agent="Mozilla/5.0 (Linux; Android 11; Pixel 4 XL)"
        CSS Width, CSS Height, Pixel-Ratio:   --metrics="360,640,2"
"""
from seleniumbase import BaseCase

if __name__ == "__main__":
    from pytest import main
    main([__file__, "--mobile", "--edge", "-s"])


class SkypeTests(BaseCase):
    def test_skype_mobile_site(self):
        if not self.mobile_emulator:
            self.open_if_not_url("about:blank")
            print("\n  This test is only for mobile-device web browsers!")
            print('  (Use "--mobile" to run this test in Mobile Mode!)')
            self.skip('Use "--mobile" to run this test in Mobile Mode!')
        self.open("https://www.skype.com/en/get-skype/")
        self.assert_element('[aria-label="Microsoft"]')
        self.assert_text("Download Skype", "h1")
        self.highlight("div.appBannerContent")
        self.highlight("h1")
        self.assert_text("Skype for Mobile", "h2")
        self.highlight("h2")
        self.highlight("#get-skype-0")
        self.highlight_click('[data-bi-name="arrow-dropdown-mobile"]')
        self.highlight("#get-skype-0_android-download")
        self.highlight('[data-bi-id*="ios"]')
