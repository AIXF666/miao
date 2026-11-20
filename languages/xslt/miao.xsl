<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" encoding="UTF-8"/>
<xsl:template match="/"><xsl:call-template name="meow"><xsl:with-param name="n" select="10000"/></xsl:call-template></xsl:template>
<xsl:template name="meow"><xsl:param name="n"/><xsl:choose><xsl:when test="$n = 1"><xsl:text>喵</xsl:text></xsl:when><xsl:when test="$n &gt; 1"><xsl:variable name="half" select="floor($n div 2)"/><xsl:call-template name="meow"><xsl:with-param name="n" select="$half"/></xsl:call-template><xsl:call-template name="meow"><xsl:with-param name="n" select="$n - $half"/></xsl:call-template></xsl:when></xsl:choose></xsl:template>
</xsl:stylesheet>
