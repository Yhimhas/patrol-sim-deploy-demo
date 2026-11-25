const button = document.querySelector("#check-api");
const result = document.querySelector("#api-result");

button.addEventListener("click", async () => {
    button.disabled = true;
    result.dataset.state = "";
    result.textContent = "正在检查 API…";

    try {
        const response = await fetch("/api/health", {
            cache: "no-store",
            signal: AbortSignal.timeout(5000),
        });
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const health = await response.json();
        if (health.status !== "ok" || typeof health.service !== "string") {
            throw new Error("健康检查响应格式不正确");
        }

        result.dataset.state = "success";
        result.textContent = `API 正常 · ${health.service}`;
    } catch (error) {
        result.dataset.state = "error";
        result.textContent = `API 检查失败 · ${error.message}`;
    } finally {
        button.disabled = false;
    }
});
