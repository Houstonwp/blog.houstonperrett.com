---
title: Newsletter 11
date: 2020-01-12
tags: ["newsletter"]
---

How do we balance the benefits and drawbacks of automation and abstraction? I've taken a 'more is better' approach in the past, but a few of this week's articles have made me reconsider. [Ironies of automation](https://blog.acolyer.org/2020/01/08/ironies-of-automation/) and the accompanying paper discuss the costs of automation. [Goodbye, Clean Code](https://overreacted.io/goodbye-clean-code/) discusses the cost of overzealous refactoring (and the same could be said of rewrites). By trying to achieve a better process, we've traded one complexity for another. We need to have a sufficient understanding of how the pieces fit into the whole and be willing to accept the risks and costs that process improvement can bring. Something to reflect on while you go throughout your day.

Have a great week.

Houston

<!--more-->

## Books

[Kings of Capital by David Carey and John E. Morris](https://smile.amazon.com/King-Capital-Remarkable-Schwarzman-Blackstone-ebook/dp/B003E8AJXI?sa-no-redirect=1) - A thorough history of Blackstone. If you're interested in private equity firms and leveraged buyouts, this is your book. If those don't sound appealing, you should take a pass.

[Work Rules! by Laszlo Bock](https://smile.amazon.com/Work-Rules-Insights-Inside-Transform-ebook/dp/B00MEMMVB8?sa-no-redirect=1) - A detailed look at the people operations unit at Google. There's a lot to be said about how data driven Google is, and there should be no surprise that they apply that mentality to every area of the business. This was a tangible counterpart to <i>How Google Works</i> that I read a couple weeks ago. Biggest takeaway was from their Project Oxygen study which found eight attributes of a good manager:

> 1. Be a good coach.
> 2. Empower the team and do not micromanage.
> 3. Express interest/concern for team members’ success and personal well-being.
> 4. Be very productive/results-oriented.
> 5. Be a good communicator – listen and share information.
> 6. Help the team with career development.
> 7. Have a clear vision/strategy for the team.
> 8. Have important technical skills that help advise the team.

They sound like commonsense, but there's value in spending time thinking about the list explicitly and how you can improve as a manager.

## Podcasts

Some extraordinary episodes from this week:

[Designing Data-Intensive Applications – Data Models: Relational vs Document](https://www.codingblocks.net/podcast/designing-data-intensive-applications-data-models-relational-vs-document/)

[Data scientists: beware of simple metrics - Linear Digressions](http://lineardigressions.com/episodes/2019/12/22/data-scientists-beware-of-simple-metrics)

[Peter Buffet – Finding Your Note – Invest Like the Best](http://investorfieldguide.com/peterbuffett/)

[What's the hidden business behind the business? - Masters of Scale](https://mastersofscale.com/jenn-hyman-the-secret-business-behind-the-business/)

[Teddy Bears - Pessimists Archive](https://pessimists.co/teddy-bears/) - I just started listening to this podcast, and I already think highly of it.

## Videos

Gilbert Strang: Linear Algebra, Deep Learning, Teaching, and MIT OpenCourseWare

{{< youtube id="lEZPfmGCEk0" >}}

Grant Sanderson: 3Blue1Brown and the Beauty of Mathematics

{{< youtube id="U_lKUK2MCsg" >}}

Vladimir Vapnik: Statistical Learning

{{< youtube id="STFcvzoxVw4" >}}


## Articles

[Ironies of automation](https://blog.acolyer.org/2020/01/08/ironies-of-automation/)

[Ten challenges for making automation a ‘team player’ in joint human-agent activity](https://blog.acolyer.org/2020/01/10/ten-challenges-for-automation/)

[Goodbye, Clean Code](https://overreacted.io/goodbye-clean-code/)

[Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) - Anyone putting machine learning into production should also be aware of the complexity and costs it adds. I see this paper as a tangible example of <i>Ironies of Automation</i>.

> Machine learning offers a fantastically powerful toolkit for building useful complex prediction systems quickly. This paper argues it is dangerous to think of these quick wins as coming for free. Using the software engineering framework of technical debt, we find it is common to incur massive ongoing maintenance costs in real-world ML systems. We explore several ML-specific risk factors to account for in system design. These include boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, changes in the external world, and a variety of system-level anti-patterns.

[Want to make good business decisions? Learn causality](https://multithreaded.stitchfix.com/blog/2019/12/19/good-marketing-decisions/) - 

> In some organizations, earnest efforts to be “data-driven” devolve into a culture of false certainty in which the influence of metrics is dictated not by their reliability but rather by their abundance and the confidence with which they’re wielded.

[People Who Are Obsessed With Success and Prestige](https://www.bennettnotes.com/post/obsessed-with-success-and-prestige/) - I wonder how many people who follow the actuarial career path fall into this trap.

[Companies stagnate when their leaders stagnate](https://leowid.com/flying/) - 

> The question that remains: When things are not going well around you, what’s not going well inside you?  

[How To Be Successful (At Your Career, Twitter Edition)](https://mobile.twitter.com/sama/status/1214274038933020672) - Sam Altman is channeling some Paul Graham in this twitter thread. Good insights.

[François Chollet on the mislabeling of "artificial intelligence"](https://mobile.twitter.com/fchollet/status/1214392496375025664) - I wish anyone talking about "artificial intelligence" would read this. 

{{< x user="fchollet" id="1214392496375025664" >}}

[The End of the Beginning](https://stratechery.com/2020/the-end-of-the-beginning/) - I would have never thought of relating the current state of the tech industry to the automotive industry. Ben brings up interesting parallels between the two.

[From 15,000 database connections to under 100: DigitalOcean's tale of tech debt](https://blog.digitalocean.com/from-15-000-database-connections-to-under-100-digitaloceans-tale-of-tech-debt/) - Technical debt is a reality at every company. Paying down the right debt effectively is a lot more challenging.

[Code-wise, cloud-foolish: avoiding bad technology choices](https://forrestbrazeal.com/2020/01/05/code-wise-cloud-foolish-avoiding-bad-technology-choices/) - 

> Code-wise, cloud-foolish thinking uses custom code to accomplish non-differentiated tasks that cloud services already perform.

This reminds me of a [similar article](https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/) by Joel Spolsky where he defends "Not-Invented-Here Syndrome":

> If it’s a core business function — do it yourself, no matter what.

[Why I use R](https://blog.shotwell.ca/posts/why_i_use_r/) - I agree with all four of his main points:

> 1. Native data science structures
> 2. Non-standard evaluation
> 3. Packaging consensus (The glory of CRAN)
> 4. Functional programming

[Hands-On Machine Learning with R](https://bradleyboehmke.github.io/HOML/) - Available free online, this looks like a decent resource for anyone wanting to tangibly work on machine learning in R. Word of caution though: there is a lot of development going on in the "tidymodels" landscape, and this book uses some more established packages rather than something under heavy development. That's understandable, but as the modeling work by RStudio becomes more production ready, I'd expect an update to this book.

[A Country Is Not a Company](https://hbr.org/1996/01/a-country-is-not-a-company) - Hard to believe this was written in 1996. A prescient piece that is as relevant today as ever.

That's it for this week.

Are there any topics or concepts you'd like me to write more about? Send any suggestions to [hp@houstonp.com](mailto:hp@houstonp.com).

Thanks everyone who sent me links and recommendations this week. If you stumble across something interesting, send it my way! You can send any recommendations to [links@houstonp.com](mailto:links@houstonp.com).
