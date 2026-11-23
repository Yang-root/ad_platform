import axios from 'axios'

// 统一走 Vite 代理：/api -> http://localhost:8000
const http = axios.create({
  baseURL: '/api',
  timeout: 10000,
})

export function fetchHello() {
  return http.get('/hello').then((res) => res.data)
}
