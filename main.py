import streamlit as st
# from scraper import scrape_website



def render_header():
    st.title("Web Scraper 2025")
    st.write("Enter a URL to scrape its content.")


def render_inputs():
    asin = st.text_input("ASIN", placeholder="Enter the ASIN here")
    geo = st.text_input("zip/postal code", placeholder="e.g., 83980")
    domain = st.selectbox("Domain", options=[
        "com", "ca", "co.uk", "de", "fr", "it", "ae"

        ])
    return asin.strip(), geo, domain


def main():
    st.set_page_config(page_title="Web Scraper 2025", layout="wide")
    render_header()
    asin, geo, domain = render_inputs()

    if st.button("Scrape"):
        if not asin:
            st.error("Please enter a valid ASIN.")
            return
        if not geo:
            st.error("Please enter a valid zip/postal code.")
            return
        if not domain:
            st.error("Please select a valid domain.")
            return

    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping in progress..."):
            st.info("Scraping functionality is currently disabled.")
            
        # result = scrape_website(asin, geo, domain)
        # st.success("Scraping completed!")
        # st.json(result)

if __name__ == "__main__":
    main()