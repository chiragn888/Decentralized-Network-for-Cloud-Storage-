# Decentralized-Network-for-Cloud-Storage-
A decentralized Cloud Network is a model that has all features of the Cloud, it provides  Dual Layer of Security and due to distributed file storage, it becomes nearly impossible to hack into the data. The data is divided into multiple slices, the slices are individually encrypted and then sent to the service decentralised cloud. Each encrypted part is stored on a random server, this provides high security. To decrypt the data, the user has to provide the private key which was generated at client-side encryption.

# Analysis

The above model is implemented by using Firebase storage, two servers from different geographical locations were chosen. At client side, Advanced Encryption Standard(AES) using Cipher-Block Chaining(CBC) with 128-bit key is used for encryption and Keyed-hash message authentication code (HMAC) using  SHA256  for authentication.
The encrypted file is then sliced by Client Engine, nominal slice size is 15% of original file size, depending on the need, user can increase or decrease the chunk size accordingly. Slices are uploaded into the servers and retrieved parallelly, these slices are then joined and decrypted by the client-side decryption software. The file is decrypted using the combination of 128-bit AES and 128-bit SHA256 private key which were generated by client-side encryption software.

# graphs

<table>
  <tr>
    <td><img width="400" alt="Screenshot 2022-06-07 at 8 37 22 AM" src="https://user-images.githubusercontent.com/65002995/172287444-086e5104-646f-464c-b5fc-1c045b825ef5.png">
</td>
     <td><img width="400" alt="Screenshot 2022-06-07 at 8 37 41 AM" src="https://user-images.githubusercontent.com/65002995/172287475-242ff533-3df8-4756-ab9b-15e446af63b8.png">
</td>
  </tr>
  <tr>
    <td><img width="400" alt="Screenshot 2022-06-07 at 8 37 57 AM" src="https://user-images.githubusercontent.com/65002995/172287507-ebd0c226-d410-487c-9561-9415ed3c2b03.png">
</td>
    <td><img width="400" alt="Screenshot 2022-06-07 at 8 38 17 AM" src="https://user-images.githubusercontent.com/65002995/172287525-1717d2a9-b4ec-4235-bb33-d6869d7e9969.png">
</td>
  </tr>
</table>




# Setting up the FastAPI application

To set up and run the FastAPI application, follow these steps:

1. Ensure you have Python 3.6 or newer installed.
2. Install the required dependencies by running `pip install -r api/requirements.txt`.
3. Run the application using Uvicorn with the command: `uvicorn api.main:app --reload`.

You can access the API endpoints at:
- `/readme` for the README.md content.
- `/license` for the LICENSE content.





