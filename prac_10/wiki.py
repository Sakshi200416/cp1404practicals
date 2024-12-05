import wikipedia

while True:
  user_input = input("Enter page title or search phrase (blank to quit): ")

  if not user_input:
    break

  try:
    # Try to get the page
    page = wikipedia.page(user_input, autosuggest=False)

    # Print details if successful
    print(f"Title: {page.title}")
    print(f"Summary: {wikipedia.summary(page)}")
    print(f"URL: {page.url}")
  except wikipedia.DisambiguationError as e:
    print(f"We need a more specific title. Try one of the following:")
    print(e.options[:5])  # Print first 5 suggestions
  except wikipedia.PageError as e:
    print(f"Page not found! Try another search.")

print("Thank you.")