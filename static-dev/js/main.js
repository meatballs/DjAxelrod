(function() {
	$(document).ready(function() {
		$('select[multiple]').multiselect();

		setupStrategyButtons();
	});

	function setupStrategyButtons() {
		$('.strategy-button').on('click', function() {
			var inputId = $(this).data('for'),
				inputEl = $('#' + inputId),
				n = parseInt(inputEl.val() || 0);

			inputEl.val(n+1);
		});
	}
})();
