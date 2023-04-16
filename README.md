"Gra w Życie" Conwaysa to automat komórkowy, w którym siatka składa się z komórek, które mogą być "żywe" lub "martwe". W każdym kroku gry, stan komórek na siatce jest aktualizowany zgodnie z pewnymi regułami.

Reguły te są następujące:
→ Jeśli żywa komórka ma mniej niż 2 lub więcej niż 3 żywych sąsiadów, to w następnej kolejności staje się martwa.
→ Jeśli martwa komórka ma dokładnie 3 żywych sąsiadów, to w następnej kolejności staje się żywa.
→ W pozostałych przypadkach komórka pozostaje w tym samym stanie.

Aby rozpocząć grę, należy wywołać funkcję main. Funkcja ta utworzy nową instancję gry oraz widoku i kontrolera oraz uruchomi pętlę główną programu. W pętli głównej programu wyświetlane są aktualne stany komórek na ekranie oraz aktualizowane są stany komórek zgodnie z regułami gry.

Możesz zmienić ustawienia gry poprzez przekazanie różnych parametrów do funkcji main, które początkowo są ustawione na : size=50, num_alive=500 oraz cell_size=15.

Parametr size określa rozmiar siatki gry czyli domyślnie 50x50 komórek, num_alive określa liczbę początkowo "żywych" komórek czyli domyślnie 500, a cell_size rozmiar jednej komórki ustawiony domyślnie na 15.

Możesz również zatrzymać i wznowić grę naciskając klawisz spacji, jednak po 1 sekundzie po zatrzymaniu gry zostanie ona automatycznie wznowiona.

Miłej zabawy!
