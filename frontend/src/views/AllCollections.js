import React from 'react';
import CollectionBlock from '../components/AllCollections/CollectionBlock';

const CollectionData = [
  {
    id: 'id1',
    title: '英雄聯盟',
    collectionUrl: '1',
    productsData: [
      {
        id: 1,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 2,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾2',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
      {
        id: 3,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾3',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 4,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾4',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
      {
        id: 5,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾5',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 6,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾6',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
    ],
  },
  {
    id: 'id2',
    title: '漫威系列',
    collectionUrl: '2',
    productsData: [
      {
        id: 1,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 2,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾2',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
      {
        id: 3,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾3',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 4,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾4',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
      {
        id: 5,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾5',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://cf.shopee.tw/file/ad118a574093b7d6ccbe469bfd0ec3a1',
      },
      {
        id: 6,
        name: '英雄聯盟 世界大賽官方正版公仔 脈衝火焰 伊澤瑞爾6',
        price: 1000,
        originPrice: 2000,
        imgUrl: 'https://img.ruten.com.tw/s2/3/74/c8/21822100524232_188.jpg',
      },
    ],
  },
];

const AllCollections = () => {

  const collections = CollectionData.map((collection) => {
    return (
      <CollectionBlock
        key={collection.id}
        id={collection.id}
        title={collection.title}
        productsData={collection.productsData}
        collectionUrl={collection.collectionUrl}
      />
    )
  });

  return (
    <div id="all_collections">
      <div className="container">
        {collections}
      </div>
    </div>
  );
}

export default AllCollections;