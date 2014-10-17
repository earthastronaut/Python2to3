# Summary of Python 3 Q & A 

This is a summary of 
[Python 3 Q & A](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html)
written by Nick Coghlan (last updated : 4th August, 2014)

Which was –– as of writing this –– last updated: unknown

I wrote this because Nick Coghlan's piece was very informative but a major time investment (~31000 words). I wanted others to have the main ideas without the barrier of the time commitment. The scope of this summary was to provide the central concepts and links alongside Coghlan's piece so they have the option for more details. I hope you find this useful
- [Dylan Gregersen](http://astrodsg.github.io)
Created : Oct 6, 2014

Other resources I found useful regarding Python 3:
* [What's New in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html) – for most of the Python 2.7 to Python 3 changes. 
* [What's New](https://docs.python.org/3/whatsnew/) – for a VERY long list of everything new (though check out the dense but "short" summary)
* [Pragmatic Unicode talk/essay](http://nedbatchelder.com/text/unipain.html) – or "Why Python 3 Exists" - Coghlan
* [Python 3 Porting Guide](http://docs.pythonsprints.com/python3_porting/py-porting.html) – nice quick reference for things which have changed from 2.x to 3x
* [Porting to Python 3: An in-depth guide](http://python3porting.com/)


---

# [Python 3 Q &amp; A](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#python-3-q-a)

Are the python core developers acting in the best interest of the community by introducing backwards incompatibly? Thoughts and rational from core python developer Nick Coghlan. He takes sole responsibility for content. However, he notes that all core developers (including Guido) _have_ reviewed and mostly agree on major points.

## [TL;DR Version](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#tl-dr-version)

The python core developers have received plenty of heated responses about breaking backwards compatibility. In this section, Coghlan lists defensive arguments regarding that choice.

## [Why was Python 3 made incompatible with Python 2?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-was-python-3-made-incompatible-with-python-2)

This section contains the rational for why backwards compatibility was broken to make Python 3 (the offensive version of the previous section). 

>According to Guido, he initiated the Python 3 project to clean up a variety of issues...[including] the removal of classic classes, changing integer division to automatically promote to a floating point result (retaining the separate floor division operation) and changing the core string type to be based on Unicode by default.

The unicode change turned out to be the change that would be hardest (not worth it) to make through the python 2 deprecation cycle. 

> The general guiding philosophy of the text model in Python 3 is essentially:
>
> * try to do the right thing by default
> * if we can’t figure out the right thing to do, throw an exception
> * as far as is practical, always require users to opt in to behaviours that pose a significant risk of silently corrupting data in non-ASCII compatible encodings

> Ned Batchelder’s wonderful [Pragmatic Unicode talk/essay](http://nedbatchelder.com/text/unipain.html) could just as well be titled “This is why Python 3 exists”.

Read/listen to Ned Batchelder's talk for a great overview of the problems with python 2 text model and why we should all be happy about python 3 unicode based text model. Batchelder's talk overlaps with the rest of the material from this section.

## [What actually changed in the text model between Python 2 and Python 3?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-actually-changed-in-the-text-model-between-python-2-and-python-3)

This section is mostly about the Unicode changes. Again read/see Ned Batchelder’s [Pragmatic Unicode](http://nedbatchelder.com/text/unipain.html) talk for a good overview.

> The Python 2 core text model looks like this:
> 
> * `str`: 8-bit type containing binary data, or encoded text data in an unknown (hopefully ASCII compatible) encoding, represented as length 1 8-bit strings
> * `unicode`: 16-bit or 32-bit type (depending on build options) containing Unicode code points, represented as length 1 Unicode strings
>

>Python 3 changes the core text model to be one that is more appropriate for application code rather than boundary code:
>
> * `str`: a sequence of Unicode code points, represented as length 1 strings (always contains text data)
> * `bytes`: a sequence of integers between 0 and 255 inclusive (always contains arbitrary binary data). While it still has many operations that are designed to make it convenient to work on ASCII compatible segments in binary data formats, it is not implicitly interoperable with the str type.


Coghlan givs a list of challenges in python 3 because of the Unicode text model. This lists the "key" sources of friction "when it comes to Python 3 between the Python core developers and other experts that have fully mastered the Python 2 text model, especially those that focus on targeting POSIX platforms rather than Windows or the JVM, as well as those that focus on writing boundary code, such as networking libraries, web frameworks and file format parsers and generators." Most programmers don't directly deal with or master writing encoding/decoding boundary code so these don't apply.

## [Why not just assume UTF-8 and avoid having to decode at system boundaries?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-not-just-assume-utf-8-and-avoid-having-to-decode-at-system-boundaries)

Coghlan gives a historic view about the str, bytes, bytearrays, and unicode types. He gives these in reference to the CPython API.


 Again read/see Ned Batchelder’s [Pragmatic Unicode](http://nedbatchelder.com/text/unipain.html) talk, especially for "Fact of life #4 : Can't infer encodings".

> The current Python 3 text model certainly has its challenges, especially around Linux compatibility (see [PEP 383](http://www.python.org/dev/peps/pep-0383) for an example of the complexity associated with that problem), but those are considered the lesser evil when compared to the alternative of breaking C extension compatibility and having to rewrite all the string manipulation algorithms to handle a variable width internal encoding, while still facing significant integration challenges on both Windows and Linux.

## [OK, that explains Unicode, but what about all the other incompatible changes?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#ok-that-explains-unicode-but-what-about-all-the-other-incompatible-changes)

> The other backwards incompatible changes in Python 3 largely fell into the following categories:
> 
> * dropping deprecated features that were frequent sources of bugs in Python 2, or had been replaced by superior alternatives and retained solely for backwards compatibility
> * reducing the number of statements in the language
> * replacing concrete list and dict objects with more memory efficient alternatives
> * renaming modules to be more PEP 8 compliant and to automatically use C accelerators when available

"The first of those were aimed at making the language easier to learn, and easier to maintain". You don't need to learn or remember to teach python 2 quirks because they've been largely fixed. See later section [Is Python 3 a better language to teach beginning programmers?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#is-python-3-a-better-language-to-teach-beginning-programmers)

Python's core API's were designed _before_ the introduction of the iterator protocol meaning a log of unnecessary lists were being created. Increased use of iterators/generators and views makes default Python 3 more memory efficient without the work required to do the same in Python 2.

Removing deprecated and renaming features makes the language smaller and easier to learn.

By and large these changes were thought through carefully and motivated.


## [What other notable changes in Python 3 depend on the text model change?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-other-notable-changes-in-python-3-depend-on-the-text-model-change)

Brief list of "enhancements in Python 3 that would likely be prohibitively difficult to backport to Python 2"

See later section [Is Python 3 a better language to teach beginning programmers?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#is-python-3-a-better-language-to-teach-beginning-programmers) for specific examples. Also the [What's New in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html) written by Guido which gives the specific changes.

## [What are (or were) some of the key dates in the Python 3 transition?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-are-or-were-some-of-the-key-dates-in-the-python-3-transition)

Gives a month/year timeline of when certain decisions were made. One takeaway: Python 3 has commercial (e.g. Red Hat Enterprise Linux, Ubuntu) support currently and in the near future. Many key packages have already switched and have dual support. Red Hat 7 was released with Python 2.7 as system default which means it will be supported until *at least* 2024.

Request for people to track down certain dates; specifically, dates when some key python packages ported to 3.


## [When can we expect Python 3 to be the obvious choice for new projects?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#when-can-we-expect-python-3-to-be-the-obvious-choice-for-new-projects)

> Going in to this transition process, my personal estimate was that it would take roughly 5 years to get from the first production ready release of Python 3 to the point where its ecosystem would be sufficiently mature for it to be recommended unreservedly for all new Python projects.

Currently "key parts of the ecosystem have successfully added Python 3 support. ". Packages like NumPy, PyGame, Django, Flask, py2exe, py2app, etc. all have python 3 support. A projects [Python 3 Readiness](http://py3readiness.org/) and [Can I use Python 3](https://pypi.python.org/pypi/caniusepython3) will inform you what packages are and aren't now Python 3.

"I think Python 3.4 is a superior language to 2.7 in almost every way". Though he also notes that there are a few things which still need to be worked out.

> However, it’s become clear that my original timeline was overly optimistic.

## [When can we expect Python 2 to be a purely historical relic?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#when-can-we-expect-python-2-to-be-a-purely-historical-relic)

"Python 2 is still a good language. While I think Python 3 is a better language". Python 2 will remain reasonably common especially since there is commercial support (e.g. Red Hat will provide support until *at least* 2024).


## [But uptake is so slow, doesn&#8217;t this mean Python 3 is failing as a platform?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#but-uptake-is-so-slow-doesn-t-this-mean-python-3-is-failing-as-a-platform)

Coghlan observes that people who declare Python 3 is a "failure" and will kill the momentum of Python don't quite understand the "key questions the transition plan is aiming to change the answers" to: 

> * “I am interested in learning Python. Should I learn Python 2 or Python 3?”
> * “I am teaching a Python class. Should I teach Python 2 or Python 3?”
> * “I am an experienced Python developer starting a new project. Should I use Python 2 or Python 3?”

"""At the start of the migration, the answer to all of those questions was obviously “Python 2”. Right now (May 2014), I believe the answer is “Python 3.4, unless you have a compelling reason to choose Python 2 instead”.""" He continues with some examples of compelling reasons. 

Many [major packages have already switched](http://py3readiness.org/). If you have a package others rely upon: Make the switch now. If you embed Python 2.7 into an application package that's fine by the core developers (though you have to maintain security updates).

The community is supportive with packages to help migration. Coghlan lists some examples. Tools to help migration he notes: [six](http://pypi.python.org/pypi/six), [lib2to3](https://docs.python.org/2/library/2to3.html), [python-modernize](https://github.com/mitsuhiko/python-modernize), [python-future](http://python-future.org/index.html), and the porting guide [Porting to Python 3: An in-depth guide](http://python3porting.com/)

Coghlan give convincing evidence that the community is in-fact taking up the mantle and making the change. e.g. "~70% of major packages now support Python 3", "Python 3 downloads outnumber Python 2 downloads (54% vs 46%)". Some developers are now even demanding the development team be more aggressive in forcing the switch. 


## [Is the ultimate success of Python 3 as a platform assured?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#is-the-ultimate-success-of-python-3-as-a-platform-assured)

Coghlan says optimistically yes, moderately “'not quite yet, but I think the outlook is very positive'”. Particularly he points to : 1) the adoption of Python3 as default by Ubuntu and Fedora so that Python 3 is now embedded into these operating systems. 2) the ongoing Python 3 porting on major projects (e.g. NumPy). 3) the number of Python 3 specific workshops by Python community organizers.

Python 3 does effect boundary system programmers (who do encoding/decoding) the most, requiring them to change code which impacts them very little. The web development community has probably had the hardest time. They mostly have to change certain problems of a faulty framework (for which they had work-arounds) for a good framework which has other problems. 

## [Python 3 is meant to make Unicode easier, so why is &lt;X&gt; harder?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#python-3-is-meant-to-make-unicode-easier-so-why-is-x-harder)

Python 3 Unicode support is still a work in progress. Probably ~3 years that the programmers most effected (web framework developers) have had a working WSGI target. Their feedback has resulted in "major improvements in the Unicode support for the Python 3.2, 3.3, and 3.4 releases." Coghlan notes that the 3.4 release is "the first one where the transition feels close to being 'done'...[for] the standard library". Though some more work needs to be completed.

Resources by Coghlan on the Python 3 text model: [Python 3 and ASCII Compatible Binary Protocols](http://python-notes.curiousefficiency.org/en/latest/python3/binary_protocols.html#binary-protocols) and [Processing Text Files in Python 3](http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html#py3k-text-files)


## [Python 3 is meant to fix Unicode, so why is &lt;X&gt; still broken?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#python-3-is-meant-to-fix-unicode-so-why-is-x-still-broken)

Computers are still generally better at dealing with English (and languages with a few limited characters) than the full flexibility of human language. Unicode signifies a major step in globalizing computers. The Python 3 unicode based text model has some tension with other text models (e.g. [Windows](http://bugs.python.org/issue1602), [POSIX](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#posix-systems)) and still needs work to fully interface with other interfaces (e.g. [WSGI middleware](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#wsgi-status).

## [Is Python 3 a better language to teach beginning programmers?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#is-python-3-a-better-language-to-teach-beginning-programmers)

"I believe so, yes, especially if teaching folks that aren’t native English speakers." Then back learn Python 2. 

I enjoyed this section and would recommend reading it in full. He gives headaches in Python 2 and what fixes them in Python 3. This compliments Guido's [What's New in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html) with a more problem-solution focus. (Don't forget to check the new things too not just fixes, e.g. [10 awesome features of Python that you can't use because you refuse to upgrade to Python 3](http://asmeurer.github.io/python3-presentation/slides.html#29)


## [Out of the box, why is Python 3 better than Python 2?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#out-of-the-box-why-is-python-3-better-than-python-2)

No significant development has gone to Python 2 since April 2010 (except some network security updates). Python 2 is a mature and capable language with a large library of support modules. Python 2 will also be supported (as it stands with 2.7) until *at least* 2024.  


## [Is Python 3 more convenient than Python 2 in every respect?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#is-python-3-more-convenient-than-python-2-in-every-respect)


## [What&#8217;s up with WSGI in Python 3?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-s-up-with-wsgi-in-python-3)


## [What&#8217;s up with POSIX systems in Python 3?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-s-up-with-posix-systems-in-python-3)


## [What changes in Python 3 have been made specifically to simplify migration?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-changes-in-python-3-have-been-made-specifically-to-simplify-migration)


## [What other changes have occurred that simplify migration?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-other-changes-have-occurred-that-simplify-migration)


## [What future changes in Python 3 are expected to further simplify migration?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-future-changes-in-python-3-are-expected-to-further-simplify-migration)


## [Didn&#8217;t you strand the major alternative implementations on Python 2?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#didn-t-you-strand-the-major-alternative-implementations-on-python-2)


## [Aren&#8217;t you abandoning Python 2 users?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#aren-t-you-abandoning-python-2-users)


## [What would it take to make you change your minds about the current plan?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-would-it-take-to-make-you-change-your-minds-about-the-current-plan)


## [Wouldn&#8217;t a Python 2.8 release help ease the transition?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#wouldn-t-a-python-2-8-release-help-ease-the-transition)


## [Aren&#8217;t the Stackless developers talking about creating a Stackless 2.8?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#aren-t-the-stackless-developers-talking-about-creating-a-stackless-2-8)


## [Aren&#8217;t you concerned Python 2 users will abandon Python over this?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#aren-t-you-concerned-python-2-users-will-abandon-python-over-this)


## [Doesn&#8217;t this make Python look like an immature and unstable platform?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#doesn-t-this-make-python-look-like-an-immature-and-unstable-platform)


## [Why wasn&#8217;t <strong>I</strong> consulted?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-wasn-t-i-consulted)


## [But &lt;name&gt; says Python 3 was a waste of time/didn&#8217;t help/made things worse!](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#but-name-says-python-3-was-a-waste-of-time-didn-t-help-made-things-worse)


## [But, but, surely fixing the GIL is more important than fixing Unicode...](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#but-but-surely-fixing-the-gil-is-more-important-than-fixing-unicode)


### [Why is using a Global Interpreter Lock (GIL) a problem?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-is-using-a-global-interpreter-lock-gil-a-problem)


### [What alternative approaches are available?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-alternative-approaches-are-available)


### [Why doesn&#8217;t this limitation really bother the core development team?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-doesn-t-this-limitation-really-bother-the-core-development-team)


### [Why isn&#8217;t &#8220;just remove the GIL&#8221; the obvious answer?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-isn-t-just-remove-the-gil-the-obvious-answer)


### [What does the future look like for concurrency in Python?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-does-the-future-look-like-for-concurrency-in-python)


## [Well, why not just add JIT compilation, then?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#well-why-not-just-add-jit-compilation-then)


## [What about &lt;insert other shiny new feature here&gt;?](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-about-insert-other-shiny-new-feature-here)

