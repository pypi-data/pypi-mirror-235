### Streamlit st-img-carousel component

Streamlit component for image-carousel:

#### Installation:

Install the component with : `pip install st-img-carousel`


#### Example:

```python

from st_img_carousel import img_carousel

def main():

    image_urls = [

    ]
    selected_img_url = img_carousel(image_urls=image_urls, height=200)

    if selected_img_url is not None:
        st.image(selected_img_url)

if __name__ == "__main__":
    main()
```

