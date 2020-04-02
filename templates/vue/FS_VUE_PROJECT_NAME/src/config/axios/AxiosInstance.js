import axios from 'axios'
import { getCookie } from 'tiny-cookie'
import { axiosConfig } from '@/config/GlobalConfig.js'


const baseConfig = {
  baseURL: axiosConfig.apiBaseURL,
  headers: {
    'Content-Type': 'application/json'
  }
}

export const axiosAPI = axios.create(baseConfig)


var instanceCSRF = axios.create(baseConfig)

instanceCSRF.interceptors.request.use(
  (config) => {
    config.headers = {
      ...config.headers,
      'X-CSRFToken': getCookie('csrftoken')
    }

    config.withCredentials = true

    return config
  },
  (error) => Promise.reject(error)
)

export const axiosCSRF = instanceCSRF
