import requests


def search_restaurants(
    cuisine=None, price_range=None, location=None, feature=None, order_by=None
):
    """
    Searches for restuarants based on cuisine, price range, location, features and order_by paramters.
    """
    headers = {}
    params = {
        "term": cuisine if cuisine else "restaurants",
        "location": location if location else "New York",
        "price": price_range if price_range else None,
        "sort_by": "rating" if not order_by else order_by,
    }

    url = "https://api.yelp.com/v3/businesses/search"

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        businesses = response.json().get("businesses", [])
        # Format the business data as required
        formatted_results = []
        for business in businesses:
            formatted_results.append(
                {
                    "name": business["name"],
                    "address": f"{business['location']['address1']}, {business['location']['city']}, {business['location']['state']}, {business['location']['zip_code']}",
                    "rating": business["rating"],
                    "description": business.get(
                        "categories", [{"title": "General Restaurant"}]
                    )[0].get("title", "General Restaurant"),
                }
            )

        return formatted_results
    else:
        return f"Error with Yelp API call: {response.status_code} - {response.text}"
