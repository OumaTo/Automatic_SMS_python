import streamlit as st
import os
from twilio.rest import Client

st.title("Automatic sms app")
Sender_Name = st.text_input("Sender's Name")
col1,col2 = st.columns(2)
Sender_Phone = col1.text_input('Sender Phone Number (+254..)')
Recepient_Phone = col2.text_input("Receiver's Phone Number (+254...)")
message = st.text_area("Enter Message")
send = st.button('SEND')

if send:
	if Sender_Name and Sender_Phone and Recepient_Phone and message:

		# Set environment variables for your credentials
		# Read more at http://twil.io/secure
		account_sid = " "
		auth_token = " "
		client = Client(account_sid, auth_token)
		message = client.messages.create(
		  body= f'{message}',

		  # for trial account, generate a number to sse in your twilio console
		  from_=f"{Sender_Phone}",

		  # use your registered number for the trial
		  to=f"{Recepient_Phone}" 
		)
		# print(message.sid)	

		# st.success(message.id)
		st.success(f'message sent from {Sender_Name} to {Recepient_Phone}')	
