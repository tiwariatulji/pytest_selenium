import requests
import pytest

BASE_URL = "https://9mu22gt18e.execute-api.eu-west-1.amazonaws.com/client/createmanifestationdetails"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZGVla3NoYUBza3llYWlyLnRlY2g6ZGVla3NoYUBza3ll"
}

PAYLOAD = {
    "manifestationDetails": [
        {
            "assignedAWBNumbers": "SR204053",
            "consigneeDetails": {
                "name": "Atul Singh",
                "address": {
                    "city": "Gurgaon",
                    "state": "Haryana",
                    "addressLine": "33 Sector, 123 bulding Viran Dham Gurugram, Haryana, India, Gurgaon",
                    "zipCode": 122016
                },
                "mobileNumber": 7404423007
            },
            "consignorDetails": {
                "name": "Vidhayak",
                "address": {
                    "city": "Gurgaon",
                    "state": "Haryana",
                    "addressLine": "SCO-84, First floor, Block B, Sector 56, Near Cloudnine Clinic, Opposite HUDA Community Center, Gurugram, Haryana 122001, Haryana",
                    "zipCode": 122001
                },
                "mobileNumber": 7404423007
            },
            "shipmentDetails": {
                "dimension": {"width": 10, "height": 20, "length": 15},
                "weight": 1,
                "eWayBill": "NA"
            },
            "productDetails": {
                "SKU": "Choco Mud Pie (New)",
                "price": "369",
                "quantity": 1
            },
            "invoiceDate": "2023-10-06 11:56:39",
            "invoiceNumber": "SK0000000020",
            "collectableDetails": {
                "COD": True,
                "modeOfPayment": "Cash/UPI",
                "value": 190.00
            }
        }
    ]
}

def test_create_manifestation():
    response = requests.post(BASE_URL, headers=HEADERS, json=PAYLOAD)
    
 
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"
    
   
    data = response.json()
    assert "manifestationId" in data or "status" in data, "Expected keys not found in response"
    
    
    if "manifestationDetails" in data:
        assert data["manifestationDetails"][0]["collectableDetails"]["COD"] is True
