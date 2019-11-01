import React, { useState, useEffect, createContext } from 'react';

export const AppContext = createContext();

const AppContextProvider = (props) => {
  const [cart, setCart] = useState([]);
  const [count, setCount] = useState(0);

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
    setCart(cart)
    localStorage.setItem('cart', JSON.stringify(cart))
  }

  const IncreaseProductCart = (id) => {
    const alreadyExistProduct = cart.find(e => e.id === id);
    cart.forEach(data => {
      data.quantity = alreadyExistProduct.quantity + 1
    })
    setCart(cart)
    localStorage.setItem('cart', JSON.stringify(cart))
  }

  const DecreaseProductCart = (id) => {
    const alreadyExistProduct = cart.find(e => e.id === id);
    cart.forEach(data => {
      data.quantity = alreadyExistProduct.quantity - 1
    })
    setCart(cart)
    localStorage.setItem('cart', JSON.stringify(cart))
  }

  return (
    <AppContext.Provider value={{ cart, addCart, IncreaseProductCart, DecreaseProductCart }}>
      {props.children}
    </AppContext.Provider>
  )
}

export default AppContextProvider;
