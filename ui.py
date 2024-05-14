import streamlit as st
from utils import *


def main():
    # Streamlit app title
    st.title("Receipt Extractor")
    # Streamlit tabs
    tab1, tab2 = st.tabs(["Upload Receipt", "Display the Data"])

    with tab1:
        st.header("Upload Receipt")
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display the uploaded image
            st.image(uploaded_file, caption='Uploaded Receipt', use_column_width=True)

            # Process the uploaded image
            receipt_data = openai_query(uploaded_file)

            # Display success message
            st.success("Message received successfully from the LLM.")

            # Display the JSON output
            st.json(receipt_data)

    with tab2:
        st.header("Display the Data")

        # # Connect to the database
        # conn = mysql.connector.connect(**db_config)
        # cursor = conn.cursor()
        #
        # # Fetch all records from the receipt_headers table, excluding the time column
        # cursor.execute(
        #     "SELECT store_name, slogan, address, store_manager, phone_number, transaction_id, date, cashier, subtotal, sales_tax, total, gift_card, charged_amount, card_type, auth_code, chip_read, aid, issuer, policy_id, expiration_date, survey_message, survey_website, user_id, password, eligibility_note FROM receipt_headers;")
        # headers = cursor.fetchall()
        #
        # # Display the headers in a table
        # st.subheader("Receipt Headers")
        # st.table(headers)
        #
        # # Fetch and display all records from the line_items table
        # st.subheader("Line Items")
        # cursor.execute("SELECT * FROM line_items;")
        # items = cursor.fetchall()
        # st.table(items)
        #
        # # Close the cursor and the connection
        # cursor.close()
        # conn.close()


if __name__ == "__main__":
    main()
