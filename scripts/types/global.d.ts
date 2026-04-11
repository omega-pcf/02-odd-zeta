/**
 * Global Type Declarations for External Modules
 */

declare module 'escape-latex' {
  function escape(text: string): string;
  export default escape;
}

declare module 'unicode2latex' {
  export class Transform {
    constructor(mode: 'bibtex' | 'latex');
    tolatex(text: string): string;
  }
}

declare module 'striptags' {
  function striptags(html: string, allowedTags?: string | string[], tagReplacement?: string): string;
  export default striptags;
}
