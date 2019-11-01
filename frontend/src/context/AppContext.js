import React, { useState, useEffect, createContext } from 'react';

export const AppContext = createContext();

const AppContextProvider = (props) => {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const cartData = JSON.parse(localStorage.getItem('cart')) || [];
    setCart(cartData);
  }, []);

  const addCart = ({ id, name, image, price, originPrice }) => {
    // check exist
    const alreadyExistProduct = cart.find(e => e.id === id);
    if (alreadyExistProduct) {
      cart.forEach(data => {
        data.quantity = alreadyExistProduct.quantity + 1
      })
    } else {
      cart.push({
        id,
        name,
        image,
        quantity: 1,
        special_price: price,
        original_price: originPrice,
      })
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    setCart(cart)
  }

  return (
    <AppContext.Provider value={{ cart, addCart }}>
      {props.children}
    </AppContext.Provider>
  )
}

export default AppContextProvider;
