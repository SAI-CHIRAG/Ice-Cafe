import streamlit as st
from app.database import add_flavor, get_flavors, add_allergen, get_all_allergens, add_item_cart, display_all_items,remove_item


def main():
    st.title("Welcome to Ice-Cafe!")
    st.logo("images/logo.png")

    menu = ["Home", "Add Flavor", "View Flavors", "Add Allergen", "View Allergens", "Manage Cart"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.logo("images/logo.png") 
        st.image("images/first.jpeg",width=700)
        st.text("Choose from the left menu !!")

    elif choice == "Add Flavor":
        st.balloons()
        st.subheader("Suggest a New Flavor")
        name = st.text_input("Flavor Name")
        season = st.selectbox("Season", ["Winter", "Spring", "Summer", "Fall"])
        if st.button("Add Flavor"):
            add_flavor(name, season)
            st.success(f"Added {name} for {season} season")
    
    elif choice == "View Flavors":
        st.balloons()
        st.subheader("Available Flavors")
        flavors = get_flavors()
        for flavor in flavors:
            st.write(f"{flavor[1]} ({flavor[2]})")
    
    elif choice == "Add Allergen":
        st.balloons()
        st.subheader("Add a New Allergen")
        allergen = st.text_input("Allergen")
        if st.button("Add Allergen"):
            add_allergen(allergen)
            st.success(f"Added allergen: {allergen}")
    
    elif choice == "View Allergens":
        st.balloons()
        st.subheader("Allergens List")
        allergens = get_all_allergens()
        for allergen in allergens:
            st.write(allergen[1])
    
    elif choice == "Manage Cart":
        st.subheader("Manage Your Cart")
        st.image("images/cart.jpeg", width=300)
        action = st.selectbox("Action", ["Add to Cart", "View Cart", "Remove from Cart"])
        
        if action == "Add to Cart":
            item = st.text_input("Item to Add")
            if st.button("Add to Cart"):
                add_item_cart(item)
                st.success(f"Added {item} to cart")
        
        elif action == "View Cart":
            st.subheader("Items List")
            items = display_all_items()
            for item in items:
                st.write(item[1])
        
        elif action == "Remove from Cart":
            item = st.text_input("Item to Remove")
            if st.button("Remove from Cart"):
                remove_item(item)
                st.success(f"Removed {item} from cart")

if __name__ == "__main__":
    main()
