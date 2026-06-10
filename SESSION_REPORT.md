# CXL_zh 仓库维护报告 (2026-06-07 ~ 2026-06-10)

> 由 Claude Code 协作生成. 仓库: jimwang2050/CXL_3.2_Spec. 提交: 18 次 (全部 push)

## 整体统计
- 翻译双语 rows: 3880 (5 个结构占位, 0 翻译问题)
- 图嵌入: 14/14 统一 fig_*_1.png 命名
- 紧致图: 16 (ch08 原) + 6 (ch14 原) + 809 (本次 MinerU 跑) = 831 张
- de-watermarked backup: 112 张 (.gitignore 忽略)
- 仓库大小: ~28MB → ~50MB

## 18 commit 时间线
1. `2d5b9c1` fix(ch08): 统一图嵌入与结构 (以 Part A 为模板)
2. `7509754` fix(ch10/11/12/14): 统一图嵌入命名
3. `db08082` fix(ch7): 统一图嵌入命名 + 补 Part B/C 三件套
4. `78cbb99` fix(ch01-06): 统一图嵌入命名 + 紧致裁剪方案规划
5. `34e17d8` docs(readme): 记录启发式紧致裁剪试水结果
6. `2ae362b` feat(tools): MinerU 紧致裁剪升级脚本 + README runbook
7. `ac61454` feat(figures): MinerU 紧致裁剪升级 (21 张成功)
8. `39b44c6` feat(ch08): 自动汇总 4 Part 本章目录 (Part B/D/E)
9. `d68d008` docs(readme): Ch3+Ch11 翻译精修报告 (0 真问题)
10. `671379c` docs(readme): 全 14 章翻译精修报告
11. `42d95e6` docs(readme): 记录 MinerU 第二轮跑结果
12. `f17f7c6` docs(readme): 21 张升级图双语 caption 状态确认
13. `8e6c9e3` feat(ch08): Part D/E TOC 增补 H3 子条目
14. `2501a8a` feat(figures): MinerU 紧致裁剪全部 batch 跑完
15. `ff5d26e` feat(md): 151 张 MinerU 额外图插入各 Part "图补遗" 段
16. `cb8d248` fix(ch12): 修正 Figure 12-1/2/3 img src 引用
17. `60fbcee` fix(ch10): Figure 10-1 改用 .png
18. `d8a6543` feat(ch08): 优化 139 占位 caption

## 工具链 (tools/)
- upgrade_tight_crops.py / image_mapper.py: MinerU 跑 + 提取
- translate_audit.py: 14 章翻译审计
- fix_ch12_captions.py / fix_ch10_figure_10_1.py: 单图修复
- insert_orphan_figures.py / optimize_ch08_placeholders.py: 图补遗
- scan_image_captions*.py / show_orphan_imgs.py: 检测 / 显示
- strip_watermark_multi.py: PIL 去水印
- extract_titles.py / extract_ch08_figs.py: 抽 raw 文本标题

## 飞书集成
- App cli_aa8b50d97139dcb5 后台配 IM+Wiki scope
- User OAuth (Jianming Wang) ✅
- Granted: im:message, im:message:readonly, docs:doc:readonly, wiki:wiki:readonly, offline_access
- hi 消息已发 (om_x100b6da3f81b10a0b278ef0e6b26304)
- Wiki 写需 wiki:wiki:write scope (后台未配, 改存本地)

## 已知遗留
1. 优化 ch08 137 占位 caption (raw 文本少)
2. 清理 .jpx 重复文件 (ch01/ch08/ch10)
3. 5 个结构占位清理 (Ch6/Ch7/Ch8 空 row/cell)
4. 飞书 OAuth 补 wiki write scope
5. 校对精修 Ch3 + Ch11
6. 下次 API 空闲时重跑剩余 ~275 张紧致裁剪
