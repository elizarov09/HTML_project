
window.vhs.init(window.vhsRegion);

(function () {
	document.querySelectorAll('.js--lazy-player-button').forEach(function (button) {
		button.addEventListener('click', function (event) {
			var dataset = event.target.closest('.js--vhi-root').dataset;
			event.target.closest('.js--lazy-player-image').style.display = 'none';
			var iframe = document.createElement('iframe');
			iframe.setAttribute('id', 'vhplayeriframe-' + dataset.videoHash);
			iframe.setAttribute('src', dataset.iframeSrc);
			iframe.setAttribute('class', 'vhi-iframe js--vhi-iframe');
			iframe.setAttribute('allow', 'autoplay; encrypted-media; clipboard-read; clipboard-write;');
			iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-popups allow-forms allow-downloads');
			iframe.setAttribute('allowFullScreen', '1');
			iframe.setAttribute('frameBorder', '0');
			iframe.setAttribute('scrolling', 'no');
			event.target.closest('.js--lazy-player-iframe').appendChild(iframe);
		});
	});
})();
