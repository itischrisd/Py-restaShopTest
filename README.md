<h1 align="center">
  <div>
    <img width="80" src="https://raw.githubusercontent.com/itischrisd/itis-PJATK/main/logo.svg" alt="PJAIT logo" />
  </div>
  Py-restaShopTest
</h1>

Repozytorium zawiera projekt końcowy z zajęć praktycznych z PPY (Podstawy Programowania w Pythonie) prowadzonych przez
Grzegorza Sochaja podczas studiów na [PJATK](https://www.pja.edu.pl/).

Kod jest rozpowszechniany na licencji [GPLv3](./LICENSE).

# Dokumentacja Projektu

## Przegląd

Projekt ten jest ramą do automatyzacji testów dla aplikacji internetowej sklepu online zbudowanego na platformie
PrestaShop. Używa Pythona z Selenium WebDriver oraz Behave dla realizacji testów w podejściu BDD (Behavior-Driven
Development — Rozwój Oparty na Zachowaniach). Celem jest zapewnienie szybkiego i powtarzalnego testowania, które
potwierdza, że aplikacja działa zgodnie z oczekiwaniami na każdym etapie rozwoju i wdrażania.

## Użyte Technologie

- **Python**: Interpretywalny język programowania wysokiego poziomu, popularny w automatyzacji, analizie danych i
  rozwoju webowym. Spośród standardowych bibliotek Pythona, używane są `os` oraz `time` pozwalające na tworzenie
  screenshotów oraz nadawania timestampów. Istotną rolę w przbiegu testów odgrywa również `assert`, który pozwala na
  sprawdzanie warunków i weryfikację poprawności działania aplikacji.
- **Selenium WebDriver**: Framework do automatyzacji przeglądarek, umożliwiający interakcję z aplikacjami webowymi.
  Pozwala na wykonywanie różnych akcji, takich jak klikanie, wpisywanie tekstu, czytanie zawartości, a także zarządzanie
  oknami i ramkami, w sposób niezależny od konkretnej przeglądarki.
- **Behave**: Framework dla Pythona, który umożliwia pisanie testów w języku naturalnym, wspierający podejście BDD.
  Użycie plików `.feature` pozwala na tworznie testów w formie scenariuszy, które są czytelne dla wszystkich
  zainteresowanych, także osób nietechnicznych.
- **PrestaShop**: Platforma open-source do tworzenia sklepów internetowych, która oferuje szeroki zakres funkcji,
  modułów i szablonów, które można dostosować do indywidualnych potrzeb. W ramach projektu testowaną aplikacją jest
  sklep internetowy hostowany przez Coder's Lab, ze względu na stosunkową trwałość danych w czasie oraz brak elementów
  HTML opakowujących interfejs.

## Struktura Projektu

Projekt podzielony został na strukturę plików i katalogów według poniższego schematu:

- **`features`**: Katalog wydzielający część stanowiącą logikę testów oraz ich konfigurację środoiwskową.
    - **`steps`**: Katalog zawierający pliki z definicjami kroków testowych, które są wykonywane w trakcie testów.
      Definicja każdego kroku jest zgodna z jego treścią w plikach `.feature`.
    - **`environment.py`**: Plik konfiguracyjny, w którym definiowane są ustawienia środowiskowe wspólne dla wszystkich
      testów, takie jak inicjalizacja opcji WebDrivera przed wszystkimi testami, otworzenie nowego okna dla każdego
      testu, czy zamykanie okna po każdym teście.
    - **`pliki .feature`**: Pliki z testami w formie scenariuszy, które są czytelne dla wszystkich zainteresowanych,
      także osób nietechnicznych. Treść kroku pozwala na zdefiniowanie akcji bądź rezultatu w języku naturalnym, a
      korzystanie ze składni Gherkin pozwala na skuteczne parametryzowanie testów.
- **`pages`**: Katalog zawierający pliki z klasami reprezentującymi poszczególne strony aplikacji, które są testowane.
  Podejście Page Object pozwala na zdefiniowanie elementów interfejsu użytkownika oraz akcji, które można na nich
  wykonać, oddzielając abstrakcję przebiegu testów od strukury testowanych stron.
    - **`base_page.py`**: Plik zawierający klasę bazową dla stron, która definiuje elementy i metody wspólne dla
      wszystkich stron aplikacji.
- **`screenshots`**: Katalog, w którym zapisywane są zrzuty ekranu z testów, tworzone w ramach udokumentowania
  pozytywnych i negatywnych rezultatów testów.
- **`utils`**: Katalog zawierający pliki z pomocniczymi funkcjami, które są wykorzystywane w trakcie testów.
    - **`assertions.py`**: Plik zawierający funkcje pomocnicze do sprawdzenia, czy wartości obiektów przekazanych przez
      argumenty są równe lub zawierają się w sobie. Funkcje zostały wyciągenięte do oddzielnego pliku w celu
      każdorazowego wyświetlenia wartości oczekiwanej i rzeczywistej w przypadku błędu.
    - **`screenshot.py`**: Plik narzędziowy pozwalający na tworzenie zrzutów ekranu z testów, opatrzonych nazwą oraz
      timestampem, które są zapisywane w katalogu `screenshots`.
- **`requirements.txt`**: Plik zawierający listę zależności, które są wymagane do uruchomienia projektu. Umożliwia
  instalację wszystkich wymaganych pakietów jednocześnie.

## Konfiguracja Środowiska

### Wymagania Wstępne

- Python 3.8 lub nowszy.
- pip (instalator pakietów Pythona).
- Przeglądarki internetowe (np. Chrome, Firefox).
- WebDriver dla każdej z przeglądarek (np. chromedriver dla Chrome).

### Instalacja

1. **Klonowanie repozytorium:**
   ```bash
   git clone https://example.com/your_repository.git
   cd my_selenium_project
   ```

2. **Instalacja zależności Pythona:**

    ```bash
    Skopiuj kod
    pip install -r requirements.txt
    ```

3. **Konfiguracja WebDriverów:**

   W pliku `features/environment.py` znajduje się fragment kodu, który inicjalizuje WebDrivera dla przeglądarki Chrome.
   W przypadku korzystania z innej przeglądarki, należy zmienić nazwę klasy na odpowiednią wartość (np. `Firefox` dla
   Firefoxa) oraz zainstalować odpowiedni WebDriver dla wybranej przeglądarki.

4. **Uruchamianie Testów**

   Uruchomienie testów odbywa się poprzez pakiet behave. Testy można wykonywać z linii poleceń:

    ```bash
    behave features/
   ```

   Aby uruchomić określone funkcje przy użyciu tagów:

    ```bash
    behave features/ --tags=@order
   ```

5. **Interpretacja Wyników**

   Wyniki testów są wyświetlane w konsoli, a zrzuty ekranu z testów są zapisywane w odpowiednim katalogu.

## Pozostałe Informacje

### Jak działają selektory

Selektory to kluczowe narzędzia używane w Selenium do identyfikacji elementów na stronie internetowej, z którymi chcemy
wejść w interakcję. Działają one jak precyzyjne wskazówki, które mówią przeglądarce, jak odnaleźć konkretny element HTML
na załadowanej stronie. W Selenium głównie używa się następujących typów selektorów:

- **ID**: Identyfikator elementu, który jest unikalny w obrębie całej strony internetowej.
- **Name**: Nazwa elementu, która jest unikalna w obrębie całego formularza.
- **Class Name**: Nazwa klasy elementu, która może być współdzielona przez wiele elementów na stronie.
- **XPath**: Ścieżka do elementu, która jest najbardziej elastyczna, ale również najbardziej skomplikowana.
- **CSS Selector**: Selektor CSS, który jest bardziej czytelny i krótszy niż XPath, ale mniej elastyczny.

W implementacji Selenium dla Pythona, selektory są krotkami, składjącymi się z dwóch elementów: typu selektora oraz jego
wartości.

### Jak context przechowuje stan testów

`context` w Behave to specjalny obiekt, który przekazywany jest do każdego kroku scenariusza testowego. Działa jak
pojemnik na dane, które mogą być udostępniane i modyfikowane przez różne kroki w trakcie wykonywania scenariusza. Oto
kilka kluczowych aspektów, jak context przechowuje stan testów:

- **Przechowywanie Danych**: `context` może przechowywać dowolne dane, od prostych wartości po skomplikowane obiekty,
  takie jak instancje przeglądarki czy obiekty stron (page objects). Na przykład, można zapisać wynik logowania
  użytkownika, aby później użyć go w kolejnych krokach scenariusza.
- **Dzielenie się Stanem**: Wszystkie kroki w danym scenariuszu mają dostęp do tego samego obiektu `context`, co
  umożliwia łatwe dzielenie się stanem i danymi między krokami.
- **Izolacja**: Mimo że `context` pozwala na dzielenie się danymi między krokami w ramach jednego scenariusza, jest on
  resetowany na początku każdego nowego scenariusza, co zapewnia izolację i niezależność testów.

---

Jeśli potrzebujesz pomocy, zauważysz błędy lub masz pomysły na ulepszenia, śmiało skontaktuj się ze mną lub stwórz
pull request.
