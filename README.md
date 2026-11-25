# Patrol Sim 部署验收样例

广东海洋大学阳江校区人工智能协会培训班工作组使用此样例，演练从 GitHub 收件、Coolify 构建到公网发布的流程。打开页面并点击「检查 API」，即可验证静态资源、前端反向代理和后端响应。

## 本地运行

在仓库根目录运行以下命令。

```bash
docker compose up -d --build --wait
```

打开浏览器访问 `http://127.0.0.1:22001/`。前端容器监听 `8080`，通过 Compose 网络访问后端的 `8000` 端口。

如需更改配置，将 `.env.example` 复制为 `.env`。`SMOKE_HTTP_BIND` 和 `SMOKE_HTTP_PORT` 控制宿主机监听地址和端口，`SMOKE_NAME` 会随 API 响应返回，便于确认环境变量已注入。完成本地验收后执行 `docker compose down`。

## Coolify 导入

1. 用此样例的 GitHub 仓库链接创建 **Public Git Repository** 应用，选择包含样例的部署分支。
2. 构建方式选择 **Docker Compose**，Base Directory 填 `/`，Compose Location 填 `/compose.yaml`。
3. 保留默认回环绑定进行服务器本机验证。需要 OpenResty 跨主机访问时，按工作组分配的内网地址和端口填写 `SMOKE_HTTP_BIND`、`SMOKE_HTTP_PORT`，并核对网关可达性。
4. 手动部署，记录部署的 commit。接入测试域名后，用域名重复以下检查。

## 验收检查

| 检查项 | 预期结果 |
| --- | --- |
| `GET /` | HTTP 200，显示「Patrol Sim 部署验收」 |
| `GET /app.js` | HTTP 200，浏览器可以加载检查脚本 |
| `GET /api/health` | HTTP 200，返回 `{"status":"ok","service":"patrol-sim-smoke"}`，其中 `service` 随 `SMOKE_NAME` 变化 |
| 点击「检查 API」 | 页面显示「API 正常」及服务标识 |
