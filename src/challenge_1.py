# From 2 inputs, business_id y zip_code.
# Perform a request to https://data.sfgov.org/resource/pyih-qa8i.json.
# Filter above inputs.
# Show business_id, business_name e inspection_score of those elements with more than 90 Score.
import http.client
import json

if __name__ == '__main__':
    business_id = "34591"
    business_postal_code = '94124'

    conn = http.client.HTTPSConnection("data.sfgov.org")
    conn.request("GET", "/resource/pyih-qa8i.json")
    response = json.loads(conn.getresponse().read().decode())

    filtered_elements = list(filter(lambda x: x['business_id'] == business_id and x['business_postal_code'] == business_postal_code, response))
    for e in filtered_elements:
        print(f"(business_id: {e['business_id']}, business_name: {e['business_name']}, inspection_score: {e['inspection_score']})")

    filtered_score = list(filter(lambda x: int(x['inspection_score']) > 90, filtered_elements))
    for e in filtered_score:
        print(f"(business_id: {e['business_id']}, business_name: {e['business_name']}, inspection_score: {e['inspection_score']})")

    conn.close()

