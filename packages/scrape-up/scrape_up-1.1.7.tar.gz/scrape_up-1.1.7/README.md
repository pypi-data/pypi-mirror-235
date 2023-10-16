## 🕷️ Scrape Up

An alternative to APIs, Scrape Up is a Python package for web scraping. It allows you to extract data from platforms like GitHub, Twitter, Instagram, or any other website that contains valuable information. It enables you to gather data through programming.

<div align="center">
  <br>
  <img src="https://img.shields.io/github/repo-size/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-closed-raw/Clueless-Community/scrape-up?style=for-the-badge" />
  <br>
  <img src="https://img.shields.io/github/forks/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr-closed-raw/Clueless-Community/scrape-up?style=for-the-badge" />
  <br>
  <img src="https://img.shields.io/github/stars/Clueless-Community/scrape-up?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/Clueless-Community/scrape-up?style=for-the-badge" />
</div>

---

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Terms and conditions for use, reproduction, and distribution are under the [MIT License](https://opensource.org/license/mit/).


----

## Contribute to this project under Hacktoberfest 2023
![image](https://github.com/Clueless-Community/scrape-up/assets/93156825/0da5aa25-06db-465b-9d31-cafe48a02ffa)

### What is Hacktoberfest? 🤔 

  Every year, DigitalOcean hosts Hacktoberfest to encourage individuals to contribute to open source **throughout October**. The main goals of Hacktoberfest are to support open-source projects, improve skills, and 
  celebrate all that is **open-source**, especially the people who make it so wonderful.

  Learn more about it [here](https://hacktoberfest.com/)
  
----

## Why Scrape Up? 👀

- **Flexible Scraping**: Customize and define the specific data you want to extract from different platforms.
- **Easy-to-Use**: Intuitive Python package interface for both beginners and experienced developers.
- **Multiple Platforms**: Scrape data from various platforms, including GitHub, Twitter, Instagram, and more.
- **Efficient and Fast**: Designed for efficient and reliable scraping of data from multiple sources.

## How to use it? ✨

1. Install the package using `pip`:

```bash
pip install scrape-up --upgrade
```

2. Import the required module and instantiate an object with the necessary parameters:

```python
# Import the required module
from scrape_up import github

# Instantiate an object with the username
user = github.Users(username="nikhil25803")
```

3. Call the desired method to scrape the required information. For example, to extract the number of followers of a user:

```python
# Call the followers method
followers_count = user.followers()

# Print the output
print(followers_count)
```

Output:

```
83
```

4. Explore all the available methods provided by Scrape Up on different platforms [here](https://github.com/Clueless-Community/scrape-up/blob/main/documentation.md).

Happy scrapping! 🕸️

## The goal 🎯

In our project journey, we encountered several challenges, including requesting timeouts and rate limits. To overcome these limitations, we developed a powerful Python tool based on web scraping. Our goal is to provide an alternative to APIs for extracting data from various platforms, including GitHub, Twitter, Instagram, and any other website that contains valuable information. Here's what our project aims to achieve:

With our web-scraping-based Python tool, you can unlock a world of data and overcome the limitations often encountered when relying solely on APIs.

## ✨ Thank You for Your Contribution!

<div align="center">
  <a href="https://github.com/Clueless-Community/scrape-up/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=Clueless-Community/scrape-up" alt="Contributors" />
  </a>
</div>


🌟 We value the time and effort you put into contributing, and we look forward to reviewing and merging your contributions. Together, let's make web scraping a powerful and accessible tool for extracting data from various platforms.

✨ Thank you for your contribution!

---

<p align="right">(<a href="#top">Back to top</a>)</p>
