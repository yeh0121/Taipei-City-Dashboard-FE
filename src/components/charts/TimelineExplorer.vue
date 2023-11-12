<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
// const props = defineProps([
// 	"chart_config",
// 	"activeChart",
// 	"series",
// 	"map_config",
// ]);
</script>

<template>
	<div v-if="activeChart === 'TimelineExplorer'">
		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>

		<div class="activity-detail">
			<div class="activity-name">2023繽紛耶誕玩台北｜北投區</div>
			<div class="activity-date">2023-11-17 ~ 2024-01-01</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.activity {
	&-detail {
		padding: calc(var(--font-m) / 2);
		background-color: #4d4d4d;
		border-radius: 5px;
		margin: 12px 5px;
	}
	&-name {
		margin-bottom: calc(var(--font-m) / 4);
	}
	&-date {
		font-size: var(--font-s);
	}
}
</style>
