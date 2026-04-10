class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Customer(BaseModel):
    name: str
    address: Address        # nested!

# Access with: customer.address.city