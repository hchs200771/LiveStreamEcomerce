import React from 'react';
import CollectionProduct from '../components/CollectionProduct'
import banner from '../assets/img/avengers.jpg'

import '../assets/scss/collection.scss'

const AllCollections = [
  {
    id: 1,
    name: '英雄聯盟',
  },
  {
    id: 2,
    name: '漫威系列',
  },
  {
    id: 3,
    name: 'DC 系列',
  },
]

const CollectionData = [
  {
    id: 1,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
    productHandle: '000',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
  {
    id: 2,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾2',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
    productHandle: '001',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
  {
    id: 3,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾3',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
    productHandle: '002',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
  {
    id: 4,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾4',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
    productHandle: '003',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
  {
    id: 5,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾5',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
    productHandle: '004',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
  {
    id: 6,
    name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾6',
    price: 1000,
    originPrice: 2000,
    imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
    productHandle: '005',
    category_collection: [
      {
        id: '1',
        name: '英雄聯盟',
      }
    ],
  },
];

const Collection = (props) => {
  const currentCollection = AllCollections.find(a => {
    return a.id === Number(props.match.params.id)
  })
  const products = CollectionData.map(product => {
    return (
      <div className="col-lg-4 col-md-6">
        <CollectionProduct
          key={product.id}
          imgUrl={product.imgUrl}
          name={product.name}
          price={product.price}
          originPrice={product.originPrice}
          id={product.id}
        />
      </div>
    );
  }); 
  return (
    <div id="collection">
      <div className="container">
        <div className="collection_banner">
          <img src={banner} />
        </div>
        <div className="row">
          <div className="side_menu col-lg-3 col-md-4">
            <div className="head">分類選單</div>
            <ul>
              {
                AllCollections.map( AllCollection => {
                  return (
                    <li key={AllCollection.id}>
                      <a className={AllCollection.id == currentCollection.id ? 'active': ''} href={AllCollection.id}>{AllCollection.name}</a>
                    </li>
                  )
                })
              }
            </ul>
          </div>
          <div className="col-lg-9 col-md-8">
            <div className="head">{currentCollection.name}</div>
            <div className="products row">
              {products}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Collection;