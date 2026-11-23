<script setup>
import { onMounted, ref } from 'vue'

import { fetchHello } from './api'

const loading = ref(false)
const error = ref('')
const result = ref(null)

async function load() {
  loading.value = true
  error.value = ''
  try {
    result.value = await fetchHello()
  } catch (e) {
    error.value = e?.message || '请求失败'
    result.value = null
  } finally {
    loading.value = false
  }
}

onMounted(load)
</script>

<template>
  <main class="page">
    <header class="page-header">
      <h1>广告投放平台</h1>
      <p class="subtitle">Django + Vue3 + MySQL 工程骨架</p>
    </header>

    <section class="card">
      <div class="card-title">
        <span>前后端联调</span>
        <span class="badge" :class="{ ok: !error && result, bad: !!error }">
          {{ error ? '连接失败' : result ? '已连接' : '连接中' }}
        </span>
      </div>

      <p v-if="loading" class="hint">正在请求 /api/hello …</p>
      <p v-else-if="error" class="error">接口调用失败：{{ error }}</p>
      <template v-else-if="result">
        <p class="message">{{ result.message }}</p>
        <dl class="meta">
          <div>
            <dt>服务</dt>
            <dd>{{ result.data?.service }}</dd>
          </div>
          <div>
            <dt>服务器时间</dt>
            <dd>{{ result.data?.server_time }}</dd>
          </div>
        </dl>
      </template>

      <button class="retry" :disabled="loading" @click="load">重新请求</button>
    </section>
  </main>
</template>

<style scoped>
.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  padding: 32px;
  background: #f4f6fb;
  color: #1f2937;
  font-family: 'Microsoft YaHei', 'PingFang SC', system-ui, sans-serif;
}

.page-header {
  text-align: center;
}

.page-header h1 {
  margin: 0;
  font-size: 32px;
  letter-spacing: 2px;
}

.subtitle {
  margin: 10px 0 0;
  color: #6b7280;
  font-size: 14px;
}

.card {
  width: min(520px, 100%);
  padding: 28px 32px;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 10px 30px rgba(31, 41, 55, 0.08);
}

.card-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 16px;
  font-weight: 600;
}

.badge {
  padding: 2px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 400;
  background: #e5e7eb;
  color: #4b5563;
}

.badge.ok {
  background: #dcfce7;
  color: #15803d;
}

.badge.bad {
  background: #fee2e2;
  color: #b91c1c;
}

.message {
  margin: 24px 0 16px;
  font-size: 26px;
  font-weight: 600;
  color: #2563eb;
  text-align: center;
}

.meta {
  margin: 0;
  display: grid;
  gap: 8px;
  font-size: 13px;
  color: #4b5563;
}

.meta div {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed #e5e7eb;
  padding-bottom: 8px;
}

.meta dt {
  color: #9ca3af;
}

.meta dd {
  margin: 0;
}

.hint {
  margin: 24px 0;
  color: #6b7280;
  text-align: center;
}

.error {
  margin: 24px 0;
  color: #b91c1c;
  text-align: center;
}

.retry {
  display: block;
  margin: 20px auto 0;
  padding: 8px 24px;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: #fff;
  font-size: 14px;
  cursor: pointer;
}

.retry:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
