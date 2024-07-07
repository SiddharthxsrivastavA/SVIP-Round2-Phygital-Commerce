import random

def ar_vr_experience(customer_id, preferences):
    experiences = ['AR try-on', 'VR store tour', 'Interactive display']
    selected_experience = random.choice(experiences)
    return f"Customer {customer_id} gets a {selected_experience} based on preferences: {preferences}"

if __name__ == "__main__":
    customer_id = 12345
    preferences = {'category': 'apparel', 'style': 'casual'}
    experience = ar_vr_experience(customer_id, preferences)
    print(experience)
