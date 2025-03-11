10 March 2025
- Maybe LayoutLM for Layout Analysis
  - Consider its effectiveness on different layouts
  - Explore integration with other tools
- Steps
  - Analysis
    - Think about what's inside the image
    - Is it a dictionary? Then probably user just want a simple set of questions answer to remember vocabularies.
    - Is it containing images? Do you think it's a decorative image or something important to be remembered?
    - Extract relevant information from the layout
    - Check if answer is included in the image, if yes, use that answer, if not generate answer with asterisk that it's ai generated
    - Add user comment
    - IMPORTANT: The model should be able to handle large image (large token window), ability to extract data
    - We will need to upload image and expose it in public folder so model can access it

- Prompt
  - content_analysis
    - Get the language
    - Analyze which anki type is suitable for this image

Blocker:
- How to process base64_encoding without hitting token?


HOW TO:
- Extract image and cloze image

What I learnt:
- Look for suitable model each step