import React, { useEffect, useContext, useState } from 'react';
import '../assets/scss/cart.scss'
import DataApi from '../api/DataApi';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { AppContext } from '../context/AppContext';

const MyCart = (props) => {
  const { cart, IncreaseProductCart, DecreaseProductCart } = useContext(AppContext);
  const [custName, setCustName] = useState('')
  const [custPhone, setCustPhone] = useState('')
  const [custEmail, setCustEmail] = useState('')
  const [custAddr, setCustAddr] = useState('')
  const [paymentType, setPaymentType] = useState('')

  const createOrder = async () => {
    const cartData = JSON.parse(localStorage.getItem('cart'))
    const products = cartData.map(p => {
      return {
        id: p.id,
        quantity: p.quantity
      }
    })

    const data = await DataApi.createOrder({
      cust_name: custName,
      cust_phone: custPhone,
      cust_email: custEmail,
      cust_addr: custAddr,
      payment_type: paymentType,
      product_collection: products
    })
    props.history.push(`/cartDetail/${data.id}`);
  }

  const cartRows = cart.map((cartRow) => {
    return (
      <div className="content" key={cartRow.id}>
        <div className="items">
          <div className="product_image">
            <a href={"/products/" + cartRow.id}>
              <img src={cartRow.image} />
            </a>
          </div>
          <h2><a href={"/products/" + cartRow.id}>{cartRow.name}</a></h2>
        </div>
        <div className="quantity">
          <div className="block">
            <div className="control">
              <button className="dec" onClick={() => DecreaseProductCart(cartRow.id)}>−</button>
              <input type="text" value={cartRow.quantity} />
              <button className="inc" onClick={() => IncreaseProductCart(cartRow.id)}>＋</button>
            </div>
            <button className="remove">移除項目</button>
          </div>
        </div>
        <div className="price">${cartRow.special_price}</div>
        <div className="total">${cartRow.quantity * cartRow.special_price}</div>
      </div>
    );
  });

  const totalPrice = () => {
    let price = 0;
    cart.forEach(c => {
      price = c.special_price * c.quantity + price;
    });
    return price
  }

  return(
    <div id="cart">
      <div className="cart_head">
        <div className="container">
          <div className="row">
            <h2>
              我的購物車
              <FontAwesomeIcon icon="chevron-right" />
            </h2>
            <button className="checkout">結帳</button>
          </div>
        </div>
      </div>
      <div className="cart_body">
        <div className="container">
          <div className="table">
            <div className="table_head">
              <div className="content">
                <div className="items">項目</div>
                <div className="quantity">數量</div>
                <div className="price">價格</div>
                <div className="total">總共</div>
              </div>
            </div>
            <div className="table_body">
              {cartRows}
            </div>
          </div>
          <div className="row">
            <div className="col-md-8 col-sm-12">
              <div className="buyers_form">
                <h3>收件者資料：</h3>
                <div className="name">
                  <label>姓名：</label>
                  <input type="text" onChange={(e) => setCustName(e.target.value)}/>
                </div>
                <div className="phone">
                  <label>電話：</label>
                  <input type="text" onChange={(e) => setCustPhone(e.target.value)}/>
                </div>
                <div className="email">
                  <label>E-mail：</label>
                  <input type="email" onChange={(e) => setCustEmail(e.target.value)}/>
                </div>
                <div className="address">
                  <label>地址：</label>
                  <input type="text" onChange={(e) => setCustAddr(e.target.value)}/>
                </div>
                <div className="pay">
                  <div>
                    <label>信用卡：</label>
                    <input type="radio" name="payment" value="Credit Card" onChange={(e) => setPaymentType(e.currentTarget.value)}/>
                  </div>
                  <div>
                    <label>ATM：</label>
                    <input type="radio" name="payment" value="ATM" onChange={(e) => setPaymentType(e.currentTarget.value)}/>
                  </div>
                  <div>
                    <label>貨到付款：</label>
                    <input type="radio" name="payment" value="Pay Shipping" onChange={(e) => setPaymentType(e.currentTarget.value)}/>
                  </div>
                </div>
                <button className="checkout" onClick={() => createOrder()}>
                  <FontAwesomeIcon icon="arrow-right" />
                  馬上結帳
                </button>
              </div>
            </div>
            <div className="col-md-4 col-sm-12">
              <div className="subtotals">
                <div className="upper_block">
                  <div className="subtotal">
                    <b>小計：</b>${totalPrice()}
                  </div>
                  <div className="subtotal">
                    <b>運費：</b>$30
                  </div>
                </div>
                <div className="lower_block">
                  <div className="the_total">
                    <b>合計：</b>${totalPrice() + 30}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyCart;