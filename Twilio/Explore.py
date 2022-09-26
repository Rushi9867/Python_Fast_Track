from twilio.rest import Client 

client = Client("AC5ac07cf5d59ab42592b4e97ffae06fc3","c97aeb97cad6641a29a03d1f3897414b")

#for msg in client.messages.list():
#    print(msg.body)

msg = client.messages.create(
    to="+919867670665",
    from_= "+19804948136",
    body = "Hello form Python",)

print(f"Created a new messege:{msg.sid}")