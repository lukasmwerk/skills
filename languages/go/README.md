# Go

Go is a statically typed, compiled programming language. It was built for productivity, multicore systems and distributed computing, almost a spiritual antithesis to C++ while being heavily inspired by C. It prioritizes run-time efficiency, usability and multiprocessing.

Go is the choice for high programmer efficiency projects, especially simple modular web-services that should be concise, predictable and easily understood by anyone. Best used for API, middleware, cli apps, personal projects exploring distributed concepts and technologies.

Pros:

*   **Easy to Learn and Readable** : Extremely easy to onboard engineers, whether they know the language or not.
*   **Built around concurrency** : Distributed and parallelization is much more straight forward given how go is built around distributed computing.
*   **Mature and Supported Toolchain** : Go has solid support and a mature, simplistic toolchain.
*   **Errors as Values** : Simple error tracking that is very easy to maintain and lends itself to services.
*   **Speed** : No compromises in performance.
*   **Single Binary** : In most cases compiles to a single binary, very easy to deploy and distribute.
*   Cross Compilation and Linking is also good.

Cons:

*   **Simple** : Complex apps, heavily optimized use-cases and situations where modern concepts like templates help development speed are not suited for go.
*   **Verbose**: Simple rules can create unecessary verbosity, which in complex apps can hamper readability. Especially with error handling. Go's error handling is well suited for services, but for other cases where error handling is more varied, other languages are better.
*   **Garbage Collected** : There are workarounds, but for extreme low-latency situations like signals and financial operations, manually managed languages are much better.
*   **Deceptively Easy** : Go is incredibly easy to understand, and out of the box easy to learn, but writing high quality go is a different story and so go projects should only really be developed by teams that have developers/leads that are experienced in the language and its paradigms.
*   **Binary Size** : Not good for embedded, also not good for OS.
*   **CRUD** : Too much boilerplate you have to write.
*   **Thread Safety**: Go has no static analysis for thread safety (Race detection cannot detect races for unrun paths), that means race conditions in production.
*   **Heavy Computation** : Go can't resort to something like C.
*   **Not for data engineering** : just use Python for data and scripts.

---

**Quick Links**

*   [https://go.dev/solutions/case-studies](https://go.dev/solutions/case-studies)
*   [https://pkg.go.dev/](https://pkg.go.dev/)
*   [https://go.dev/doc/effective_go](https://go.dev/doc/effective_go)
*   [https://github.com/sinamna/road-to-Go-and-beyond](https://github.com/sinamna/road-to-Go-and-beyond)

**Notes**

**Experience**

*   Ecommerce services, ranging from small single use cases to shop implementations, working with databases, caches, channels and routines, async operations, REST APIs, callbacks, go testing, context and loggers.
*   Data pipelining service (ended up using python for the actual interaction with data, but go served well as a coordinator/interface on top of the python building blocks to connect everything and implement distribution of a main/worker system)
*   Implementation of MapReduce, with test clients and exchangeable mutation functions.
*   Implementation of Raft Consensus, fully featured.
*   Implementation of the Google File System.
*   University course assignments on reading weather stations data, bank transaction systems