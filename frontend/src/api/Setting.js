import axios from 'axios';

const client = axios.create({
  baseURL: 'https://live-ecommerce-server.herokuapp.com/api/v1',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  async execute(method, resource, data) {
    return client({
      method,
      url: resource,
      data,
    }).then(req => {
      return req.data
    }).catch(err => {
      console.log(err);
    })
  }
};