import React, { useState, useEffect } from 'react';
import '../assets/scss/cart_detail.scss';
import DataApi from '../api/DataApi';

const CartDetail = (props) => {
  const [orderInfo, setOrderInfo] = useState(null)
  useEffect(() => {
    const getOrderInfo = async () => {
      const data = await DataApi.getOrderInfo(props.match.params.id)
      setOrderInfo(data)
    }
    getOrderInfo()
  }, [props])

  const allOrders = orderInfo && orderInfo.product_collection.map(order => {
    return (
      <tr key={order.id}>
        <td>
          <img src={order.image} />
          <span className="product_name">{order.name}</span>
        </td>
        <td>NT${order.original_price}</td>
        <td>{order.quantity}</td>
        <td>NT${order.original_price * order.quantity}</td>
      </tr>
    )
  })

  return (
    <div id="cart_detail">
      <div className="container">
        <div className="row">
          <div className="col-md-12">
            <div className="header">訂單明細</div>
            <div className="description">謝謝您的購買，以下是您的訂單明細</div>
            <div className="order_number">
              訂單編號
              <span className="number">104123456</span>
            </div>
            <div className="order_info">
              <table>
                <thead>
                  <tr>
                    <th width="70%">商品名稱</th>
                    <th width="10%">單價</th>
                    <th width="10%">數量</th>
                    <th width="10%">金額</th>
                  </tr>
                </thead>
                <tbody>
                  {allOrders}
                </tbody>
              </table>
              <div className="total_price">
                NT${orderInfo && orderInfo.total}
              </div>
            </div>
            <div className="back_collections" onClick={() => props.history.push('/')}>回商品列表頁</div>
          </div>
        </div>
      </div>
    </div>
  )
};

export default CartDetail;