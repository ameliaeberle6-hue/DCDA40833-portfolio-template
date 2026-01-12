# DCDA 40833 Skills Portfolio Template

## About This Template

This template is designed specifically for DCDA 40833 students completing their final digital humanities research project. It provides a professional web portfolio structure for the **Skills Portfolio (HTML/CSS)** deliverable described in the D2L course shell.

### Project Context

This portfolio template helps you present these integrated findings to public audiences, demonstrating how computational and humanities approaches reveal insights that neither could discover alone.

---

## Getting Started

**Choose your setup guide:**
- 📖 **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Web developer and contributor setup (GitHub Desktop + VS Code)
- ⚡ **[QUICK_START.md](QUICK_START.md)** - Fast reference for content editing (5 minutes)
- 👨‍🏫 **[INSTRUCTOR_SETUP.md](INSTRUCTOR_SETUP.md)** - For instructors setting up the template

### How Weekly Lab Assignments Connect to This Portfolio


### Template Workflow

1. Click **"Use this template"** button (green button at top of repository)
2. Name your repository (e.g., `sentiment-analysis-taylor-swift`)
3. Make it **Public** (required for GitHub Pages)
4. Clone with GitHub Desktop and open in VS Code
5. Edit `index.html` following the TODO markers

---

## What's Included

```
portfolio-template/
├── index.html              ← Complete HTML template with TODO markers
├── css/
│   └── styles.css          ← Professional CSS (TCU colors, fully responsive)
├── images/                 ← Place your PNG visualizations here
│   └── .gitkeep           ← Placeholder file
├── README.md               ← This file (complete documentation)
├── QUICK_START.md          ← Fast reference guide (5-minute setup)
├── VISUAL_GUIDE.md         ← Complete step-by-step tutorial with visuals
├── INSTRUCTOR_SETUP.md     ← Instructor guide for template setup
└── .gitignore              ← Ignore temporary files
```

---

## Step-by-Step Customization

### Step 1: Edit HTML Content

Open `index.html` in your text editor (VS Code recommended) and look for `<!-- TODO: ... -->` comments. These mark exactly where to add your content.

**Quick Find & Replace:**
- `Your Name` → Your actual name (or "Team Name")
- `Your Project Title` → Your research project title
- `yourusername` → Your GitHub username (in footer)
- `project-name` → Your repository name (in footer)

### Step 2: Fill in Each Section

Coming Soon

### Step 3: Add Your Visualizations

1. **Export charts from Google Colab** as PNG files (see code example below)
2. **Save PNG files** in the `images/` folder
3. **Update image paths** in `index.html` to match your filenames

**Example: Exporting from Google Colab**

```python
import matplotlib.pyplot as plt

# Create your visualization
plt.figure(figsize=(10, 6))
# ... your plotting code ...

# Save as PNG
plt.savefig('sentiment-distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# In Colab: Files tab (left sidebar) → Right-click file → Download
# Then upload to GitHub in your portfolio's images/ folder
```

### Step 4: Include Code Examples

The template includes styled code blocks. Copy relevant Python code from your notebooks:

```html
<div class="code-title">sentiment_analysis.py</div>
<pre><code>from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
df['compound'] = df['text'].apply(
    lambda x: analyzer.polarity_scores(x)['compound']
)</code></pre>
```

### Step 5: Connect to Critical Frameworks

Use the special callout boxes to connect your work to course frameworks:

```html
<div class="framework-callout">
    <h3>📐 Classification Logic</h3>
    <p>This project demonstrates how algorithmic categorization...</p>
</div>
```

**Framework Options:**
- **📐 Classification Logic** - How algorithms categorize culture
- **🤖 AI Agency** - Power structures and pseudo-intelligence
- **🔒 Sacred Boundaries** - Privacy, ethics, digital divides
- **📚 Collective Memory** - Cultural preservation, digital archives

---

## Deploy to GitHub Pages

Make your portfolio publicly accessible in 3 steps:

1. **Go to repository Settings → Pages** (left sidebar)
2. **Source:** Select "Deploy from a branch"
3. **Branch:** Select `main` (or `master`), folder: `/ (root)`
4. **Click Save**
5. **Wait 1-2 minutes**, then visit: `https://YOUR-USERNAME.github.io/your-project-name`

**Troubleshooting:**
- Make sure repository is **Public** (Settings → General)
- Check that `index.html` is in the root directory (not in a subfolder)
- Allow 1-2 minutes for first deployment
- Refresh browser cache (Ctrl+Shift+R or Cmd+Shift+R)

---

## Working as a Group

**📖 For complete group workflow guide, see [VISUAL_GUIDE.md](VISUAL_GUIDE.md) Steps 10-15**

### GitHub Desktop Workflow (Recommended)

**Best for: Groups working on the same repository with frequent edits**

1. **Designate repository owner:**
   - Choose one person to create the repository from template
   - This person's GitHub account will host the repository
2. **Owner adds collaborators:**
   - Settings → Collaborators → Add people
   - Enter each teammate's GitHub username
   - Teammates accept email invitation
3. **Everyone clones the repository:**
   - Open GitHub Desktop
   - File → Clone Repository
   - Select the owner's repository
   - Choose local save location
4. **Follow the Golden Rule: PULL → EDIT → COMMIT → PUSH**
   - **PULL:** Always click "Fetch origin" then "Pull" before editing
   - **EDIT:** Make your changes to your assigned section
   - **COMMIT:** Add descriptive message, click "Commit to main"
   - **PUSH:** Click "Push origin" to sync changes to GitHub
5. **Coordinate sections:**
   - Assign specific sections to each person
   - Communicate before editing: "Editing Methods section now"
   - Wait for teammate to push before you start editing
6. **Handle merge conflicts:**
   - GitHub Desktop will alert you if conflicts occur
   - Open conflicted file in text editor
   - Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Choose which version to keep or combine both
   - Save file, commit, and push

### Communication is Key

**Before editing:**
```
"Pulling latest changes now"
"Editing Research Question - will take ~15 min"
```

**After editing:**
```
"Committed and pushed Methods section"
"Done! Safe to pull and edit now"
```

**Tools for coordination:**
- Slack / Discord / GroupMe / Text messages
- Regular check-ins via Zoom/Google Meet

### Division of Labor Example

**3-person group:**
- Person A: Research Question, Background → Session 1
- Person B: Data & Methods, Analysis → Session 2  
- Person C: Findings, Reflection → Session 3
- One person: Upload all images in one batch

**2-person group:**
- Person A: Research Question, Data & Methods, Reflection
- Person B: Analysis, Findings, Images

---

## Template Features (Already Built In)

### Visual Design
- ✅ **TCU Purple color scheme** (customizable in CSS)
- ✅ **Responsive design** - Works on desktop, tablet, mobile
- ✅ **Sticky navigation** - Menu stays visible while scrolling
- ✅ **Smooth scrolling** - Anchor links animate smoothly
- ✅ **Professional typography** - System fonts for fast loading

### Technical Features
- ✅ **Semantic HTML5** - Proper structure for accessibility
- ✅ **Code syntax highlighting** - Dark theme for Python code
- ✅ **Image optimization** - Responsive images with captions
- ✅ **Data tables** - Formatted results tables with highlighting
- ✅ **Print-friendly** - Portfolio prints nicely for PDF export
- ✅ **Framework callouts** - Special styling for critical reflections

### No Configuration Needed
- ✅ **CSS is complete** - No styling knowledge required
- ✅ **HTML structure is done** - Just fill in content
- ✅ **Mobile responsive** - Automatically adapts to screen size
- ✅ **Browser compatible** - Works in all modern browsers

---

## Customization (Optional)

### Change Color Scheme

Edit `css/styles.css` at the top:

```css
:root {
    --primary-color: #4d1979;      /* Main color (currently TCU Purple) */
    --secondary-color: #7c3aed;    /* Accent color */
    --accent-color: #ffd700;       /* Highlight color (currently gold) */
}
```

Try these color schemes:
- **Blue Academia:** `#1e3a8a`, `#3b82f6`, `#fbbf24`
- **Green Digital:** `#065f46`, `#10b981`, `#f59e0b`
- **Red Critical:** `#7f1d1d`, `#ef4444`, `#fcd34d`

### Add More Sections

Copy existing section structure:

```html
<section id="new-section">
    <h2>New Section Title</h2>
    <p>Your content here...</p>
</section>
```

Don't forget to add navigation link:

```html
<nav>
    <ul>
        <!-- existing links -->
        <li><a href="#new-section">New Section</a></li>
    </ul>
</nav>
```

## Content Guidelines

### Research Question Section
- State your research question clearly
- Explain why it matters
- Provide background context

### Data & Methods Section
Include:
- Data source and size
- Collection methodology
- Ethical considerations (privacy, consent, etc.)
- Analysis tools (pandas, VADER, Gensim)

### Analysis Section
Show:
- Visualizations with descriptive captions
- Code snippets demonstrating your methods
- Clear explanations of what you discovered

### Findings Section
Present:
- Key discoveries (numbered list recommended)
- Data tables with results
- Discussion of what surprised you

### Reflection Section
Address (from essay requirements):
- **Integration & Reflection:** How did your project integrate both humanities work and data analytics?
- **What computational methods revealed** that close reading alone could not
- **Connections to course frameworks:** Classification Logic, AI Agency, Sacred Boundaries, Collective Memory
- **Evolution of thinking:** How did your understanding deepen and change through engagement with data?
- **Public Presentation Strategy:** Design choices for communicating findings to non-academic audiences
- **Limitations:** What would you change if you repeated the project?
- **Future directions:** What would you pursue with additional time?
- **Confidence assessment:** How confident are you in your conclusions and why?

## Tips for Success

### Writing for Public Audiences
- **Avoid jargon** - Explain technical terms
- **Tell a story** - Guide readers through your process
- **Be honest** - Discuss limitations and uncertainties
- **Show evolution** - Explain how your thinking changed

### Technical Best Practices
- **Alt text for images** - Describe what data visualizations show
- **Descriptive captions** - Help readers interpret charts
- **Code comments** - Explain what your code does
- **TODO markers** - Use `<!-- TODO: ... -->` for incomplete sections

### Accessibility
- Use semantic HTML tags (already done in template)
- Write descriptive alt text for images
- Ensure sufficient color contrast (template already handles this)
- Test with keyboard navigation (Tab key should work)

---

## Troubleshooting

### Images Not Showing

**Problem:** Broken image icons or missing visualizations

**Solutions:**
- ✅ Verify PNG files are in `images/` folder (not `Images/` or `img/`)
- ✅ Check exact filename match (case-sensitive): `sentiment-chart.png` ≠ `Sentiment-Chart.png`
- ✅ Use relative paths: `images/chart.png` (NOT `/images/chart.png` or `C:/Users/...`)
- ✅ Refresh browser cache: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### CSS Not Loading

**Problem:** Plain HTML with no styling

**Solutions:**
- ✅ Verify `styles.css` is in `css/` folder (not root directory)
- ✅ Check `<link>` tag in `index.html` points to `css/styles.css`
- ✅ Clear browser cache and hard refresh
- ✅ Open browser developer tools (F12) and check Console for errors

### GitHub Pages Not Working

**Problem:** 404 error or site not found

**Solutions:**
- ✅ Confirm repository is **Public** (not Private)
- ✅ Verify `index.html` is in root directory (not in subfolder)
- ✅ Wait 1-2 minutes after enabling Pages
- ✅ Check Pages settings: Settings → Pages → Source should be "main branch"
- ✅ Visit exact URL: `https://username.github.io/repo-name/` (with trailing slash)

### Git Conflicts

**Problem:** "Merge conflict" when pulling or pushing

**Solutions:**
- ✅ **Don't panic!** Conflicts are normal in group work
- ✅ Talk with your group - coordinate who's editing what sections
- ✅ Use branches for separate work (see Working as a Group section)
- ✅ Ask for help in class or office hours - we'll walk through it

---

## Final Project Checklist

Use this to verify your portfolio is complete:

### Content Completeness
- [ ] Replaced all placeholder text (Your Name, Your Project Title, etc.)
- [ ] Removed or completed all `<!-- TODO: -->` comments
- [ ] Research question clearly stated with background context
- [ ] Dataset documentation includes source, size, and ethical considerations
- [ ] Analysis methods explained (VADER, Gensim, term frequency, etc.)
- [ ] At least 3 data visualizations with captions and alt text
- [ ] At least 2 code examples with explanations
- [ ] Results table with quantitative findings
- [ ] Critical reflection connects to at least 2 course frameworks
- [ ] Limitations and future directions discussed
- [ ] Footer link updated to point to your GitHub repository

### Technical Requirements
- [ ] All visualization PNG files saved in `images/` folder
- [ ] Image paths correctly point to files (no broken images)
- [ ] CSS stylesheet loading properly (page has styling)
- [ ] Navigation links work (smooth scroll to sections)
- [ ] Portfolio tested in web browser (Chrome, Firefox, or Safari)
- [ ] Mobile responsiveness checked (resize browser window)
- [ ] Committed all changes to GitHub repository
- [ ] GitHub Pages enabled and site is live
- [ ] GitHub repository link in footer works

### Group Work (if applicable)
- [ ] All group members added as repository collaborators
- [ ] Each member's contributions acknowledged
- [ ] Merged all sections together cohesively
- [ ] Resolved any merge conflicts
- [ ] Entire group reviewed final version

### Quality & Polish
- [ ] Proofread all text (spelling, grammar, punctuation)
- [ ] Consistent formatting throughout sections
- [ ] Visualizations are high quality (300 DPI recommended)
- [ ] Code examples are properly formatted and readable
- [ ] Framework connections are meaningful (not superficial)
- [ ] Reflection demonstrates genuine critical thinking
- [ ] Portfolio tells a coherent research story

---

## Alignment with Final Project Requirements

This template directly supports all four final project deliverables:

### 1. Research Essay (1500-2000 words) ✅
Portfolio sections align with essay structure:
- **Overview** → Research Question section
- **Research Question** → Research Question section  
- **Methods** → Data & Methods section
- **Findings** → Results & Analysis + Key Findings sections
- **Integration & Reflection** → Critical Reflection section
- **Public Presentation Strategy** → Addressed in reflection

### 2. Python Notebooks (.ipynb files) ✅
- Footer links to GitHub repository containing your Colab notebooks
- Code snippets embedded in Analysis section demonstrate three base methods
- Visualizations exported from notebooks displayed throughout portfolio

### 3. Dataset Documentation (CSV files + data biography) ✅
Data & Methods section includes:
- **Data sources** with proper attribution
- **Collection methodology** (Instant Data Scraper, APIs, manual collection)
- **Data biography** (250-400 words): ethical considerations, privacy, preparation steps
- **Sample size** and dataset characteristics
- **Replication instructions** for transparency

### 4. Web Portfolio (HTML/CSS) ✅
**This entire template IS your web portfolio deliverable**, meeting technical standards:
- Clean, accessible presentation for public audiences
- Integration of visualizations and analysis from notebooks
- Demonstrates HTML/CSS skills (structure provided, you customize content)
- Effective narrative structure communicating insights
- Professional presentation suitable for academic/career portfolios

---

## Assessment Philosophy Alignment

This portfolio embodies the course's assessment priorities:

> "This project prioritizes earned insight over clean code."

Your portfolio should demonstrate:
- ✅ **Depth of reflection** - Critical thinking about methods and findings
- ✅ **Willingness to be surprised** - Evolution from predictions to data-driven opinions
- ✅ **Critical assessment** - Honest evaluation of results AND analytical tools
- ✅ **Integration** - Computational analysis working with humanistic interpretation

**Remember:** Being "wrong" in your initial assumptions is not failure—it's evidence of genuine learning. The goal is not to confirm what you already thought, but to discover what emerges when computational analysis challenges cultural interpretation.

---

## Resources

### Course Materials
- **HTML/CSS Workshop** - Review Sessions 1-3 for troubleshooting
- **Semantic HTML Guide** - `semantic_html_css_workshop.html` in course repo
- **HW4-1 & HW4-2** - Reference your own notebooks for content
- **Mini-Lectures** - Review critical frameworks for reflection section

### Technical References
- **Markdown Guide:** [markdownguide.org](https://www.markdownguide.org/)
- **HTML Reference:** [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **Git Basics:** [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- **GitHub Pages:** [Official Pages Documentation](https://docs.github.com/en/pages)

### Tools
- **VS Code** (Recommended editor): [code.visualstudio.com](https://code.visualstudio.com/)
- **Google Colab:** Your notebook environment for data analysis
- **Image optimization:** Use `plt.savefig(..., dpi=300)` in Python
- **Git GUI** (if you prefer visual): [GitHub Desktop](https://desktop.github.com/)

---

## Support

### Getting Help

1. **Check QUICK_START.md** - Fast answers to common questions
2. **Review workshop materials** - HTML/CSS Sessions 1-3
3. **Test in browser** - Open Developer Tools (F12) to see errors
4. **Ask your group** - Collaborate on problem-solving
5. **Office hours** - Bring specific questions or errors
6. **Canvas discussion** - Post screenshots of issues

### Common Questions

**Q: Do I need to know CSS to use this template?**
A: No! The CSS is complete. You only need to edit `index.html` content.

**Q: Can I use this template for other projects?**
A: Yes! It's designed for digital humanities research but adaptable to any project.

**Q: What if I want a different color scheme?**
A: Edit the `:root` section in `css/styles.css` (see Customization section above).

**Q: How do I make my repository private after the class?**
A: Settings → General → Change repository visibility → Make private (after grading is complete).

**Q: Can I use this in my professional portfolio?**
A: Absolutely! That's the point. It's yours to keep and showcase.

---

## Success Criteria (from Final Project Requirements)

A successful portfolio will:

✅ **Execute an intellectually significant research question** that requires both computational and interpretive methods  
✅ **Demonstrate sophisticated use of all three base analytical methods** (term frequency, sentiment analysis, topic modeling)  
✅ **Present findings effectively** to both academic and public audiences  
✅ **Reflect critically** on the integration of digital and traditional humanities approaches  
✅ **Show clear evolution** from HW5 proposal through final execution  

### What You're Answering

Your portfolio is your answer to the course's central question:

> **What insights emerge when we integrate term frequency analysis, sentiment analysis, and topic modeling with traditional humanities interpretation methods?**

Show us:
- What computational and humanities approaches **reveal together** that neither could discover alone
- How you moved from **initial assumptions** to **well-grounded, data-driven opinions**
- What happens when **coding meets culture** in your specific research domain

---

## Philosophy: When Coding Meets Culture

This template embodies the course's core principle: **computational methods and cultural interpretation are strongest when integrated.**

Your portfolio should demonstrate:
- **Technical competence** - You can collect, clean, and analyze data with Python, VADER, and Gensim
- **Critical thinking** - You can interpret results within cultural and theoretical contexts
- **Methodological awareness** - You understand strengths AND limitations of your tools
- **Intellectual honesty** - You acknowledge uncertainty and evolution of thought
- **Public communication** - You can explain technical work to general audiences effectively

### Your Intellectual Journey Matters Most

From the project requirements:

> "Being 'wrong' in your initial assumptions is not failure—it's evidence of genuine learning and the foundation for developing well-grounded, data-driven opinions."

Focus on showing:
- How your **thinking evolved** through engagement with data and methods
- What **surprised you** and challenged your assumptions  
- How computational analysis **refined and complicated** your cultural interpretation
- Your growth as both a **computational thinker** and **humanities scholar**

---

## Credits & Support

**Template created for:**  
WRIT 20833: Introduction to Coding in the Humanities  
Fall 2025 | TCU  
[View Full Project Requirements](https://tcu-dcda.github.io/WRIT20833-2025/WRIT20833_Final_Project_Requirements.html)

**License:** MIT (you may use, modify, and share freely)

**Getting Help:**
- 📖 Review [SETUP_GUIDE.md](SETUP_GUIDE.md) for technical setup
- ⚡ Check [QUICK_START.md](QUICK_START.md) for fast content editing
- 💬 Attend office hours for one-on-one support
- 👥 Collaborate with your group on problem-solving
- 📚 Reference course materials and workshop sessions

---

**Good luck with your project!**

We're excited to see what you discover when coding meets culture in your research. Remember: this portfolio represents the culmination of your semester-long exploration of digital humanities methods. Make it yours. Tell your story. Show us what you learned.
