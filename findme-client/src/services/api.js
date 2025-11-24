import axios from 'axios';

const API_BASE_URL = process.env.NODE_ENV === 'production'
  ? 'https://findme-l00y.onrender.com/api'
  : 'http://localhost:5000/api';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Missing Persons API
export const missingPersonsAPI = {
  getAll: () => api.get('/missing-persons'),
  getById: (id) => api.get(`/missing-persons/${id}`),
  create: (data) => api.post('/missing-persons', data),
  update: (id, data) => api.put(`/missing-persons/${id}`, data),
  delete: (id) => api.delete(`/missing-persons/${id}`),
};

// Health check
export const healthCheck = () => api.get('/health');
