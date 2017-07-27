from Assets.NumberFunctions import simple_round


def form_progress_bar(interval, progress, total_progress, progress_symbol="+", empty_symbol="="):
    if progress <= total_progress:
        safe_position = simple_round(progress, interval)
        total_symbols = int(total_progress/interval)
        progress_symbols = int(safe_position/interval)
        progress_bar = []
        for i in range(0, progress_symbols):
            progress_bar.append(progress_symbol)
        for i in range(0, total_symbols-progress_symbols):
            progress_bar.append(empty_symbol)
        return("".join(progress_bar))

